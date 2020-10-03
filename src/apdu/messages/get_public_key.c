/*******************************************************************************
*    XYM Wallet
*    (c) 2020 Ledger
*    (c) 2020 FDS
*
*  Licensed under the Apache License, Version 2.0 (the "License");
*  you may not use this file except in compliance with the License.
*  You may obtain a copy of the License at
*
*      http://www.apache.org/licenses/LICENSE-2.0
*
*  Unless required by applicable law or agreed to in writing, software
*  distributed under the License is distributed on an "AS IS" BASIS,
*  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
*  See the License for the specific language governing permissions and
*  limitations under the License.
********************************************************************************/
#include "get_public_key.h"
#include "apdu/global.h"
#include "xym/xym_helpers.h"
#include "ui/main/idle_menu.h"
#include "ui/address/address_ui.h"

uint8_t xymPublicKey[XYM_PUBLIC_KEY_LENGTH];

uint32_t set_result_get_publicKey() {
    uint32_t tx = 0;
    //publicKey
    G_io_apdu_buffer[tx++] = XYM_PUBLIC_KEY_LENGTH;
    os_memmove(G_io_apdu_buffer + tx, xymPublicKey, XYM_PUBLIC_KEY_LENGTH);
    tx += 32;
    return tx;
}

void on_address_confirmed() {
    uint32_t tx = set_result_get_publicKey();
    G_io_apdu_buffer[tx++] = 0x90;
    G_io_apdu_buffer[tx++] = 0x00;
    // Send back the response, do not restart the event loop
    io_exchange(CHANNEL_APDU | IO_RETURN_AFTER_TX, tx);
    // Display back the original UX
    display_idle_menu();
}

void on_address_rejected() {
    G_io_apdu_buffer[0] = 0x69;
    G_io_apdu_buffer[1] = 0x85;
    // Send back the response, do not restart the event loop
    io_exchange(CHANNEL_APDU | IO_RETURN_AFTER_TX, 2);
    // Display back the original UX
    display_idle_menu();
}

void handle_public_key(uint8_t p1, uint8_t p2, uint8_t *dataBuffer,
                        uint16_t dataLength, volatile unsigned int *flags,
                        volatile unsigned int *tx) {
    uint8_t privateKeyData[XYM_PRIVATE_KEY_LENGTH];
    uint32_t bip32Path[MAX_BIP32_PATH];
    uint32_t i;
    uint8_t bip32PathLength = *(dataBuffer++);
    cx_ecfp_private_key_t privateKey;
    cx_ecfp_public_key_t publicKey;
    uint8_t algo;
    cx_curve_t curve;
    char address[XYM_PRETTY_ADDRESS_LENGTH+1];
    uint8_t p2Chain = p2 & 0x3F;
    UNUSED(p2Chain);

    if (dataLength != XYM_PKG_GETPUBLICKEY_LENGTH) {
        THROW(0x6a80);
    }
    if ((bip32PathLength < 0x01) || (bip32PathLength > MAX_BIP32_PATH)) {
        THROW(0x6a80);
    }
    if ((p1 != P1_CONFIRM) && (p1 != P1_NON_CONFIRM)) {
        THROW(0x6B00);
    }
    if (((p2 & P2_SECP256K1) == 0) && ((p2 & P2_ED25519) == 0)) {
        THROW(0x6B00);
    }
    if (((p2 & P2_SECP256K1) != 0) && ((p2 & P2_ED25519) != 0)) {
        THROW(0x6B00);
    }
    curve = (((p2 & P2_ED25519) != 0) ? CX_CURVE_Ed25519 : CX_CURVE_256K1);

    //Read and convert path's data
    for (i = 0; i < bip32PathLength; i++) {
        bip32Path[i] = (dataBuffer[0] << 24) | (dataBuffer[1] << 16) |
                       (dataBuffer[2] << 8) | (dataBuffer[3]);
        dataBuffer += 4;
    }
    uint8_t network_type = *dataBuffer;

    io_seproxyhal_io_heartbeat();

    BEGIN_TRY {
        TRY {
            // Changed hashing algorithm to cope with catapult-server changes. All Key derivation and signing are now using SHA512.
            // Removed SignSchema so NetworkType is no longer bonded to the schema anymore (sha3 / keccak).
            // This change will affect all existing keypairs / address (derived from public key) and transaction signatures.
            algo = CX_SHA512;
            os_perso_derive_node_bip32(CX_CURVE_256K1, bip32Path, bip32PathLength, privateKeyData, NULL);
            cx_ecfp_init_private_key(curve, privateKeyData, XYM_PRIVATE_KEY_LENGTH, &privateKey);
            io_seproxyhal_io_heartbeat();
            cx_ecfp_generate_pair2(curve,
                                    &publicKey,
                                    &privateKey,
                                    1,
                                    algo);
            explicit_bzero(&privateKey, sizeof(privateKey));
            explicit_bzero(privateKeyData, sizeof(privateKeyData));
            io_seproxyhal_io_heartbeat();
            xym_public_key_and_address(&publicKey,
                                          network_type,
                                          (uint8_t*) &xymPublicKey,
                                          (char*) &address,
                                          XYM_PRETTY_ADDRESS_LENGTH + 1
                                          );
            io_seproxyhal_io_heartbeat();
            address[XYM_PRETTY_ADDRESS_LENGTH] = '\0';
        }
        CATCH_OTHER(e) {
            THROW(e);
        }
        FINALLY {
            explicit_bzero(privateKeyData, sizeof(privateKeyData));
            explicit_bzero(&privateKey, sizeof(privateKey));
        }
    }
    END_TRY

    if (p1 == P1_NON_CONFIRM) {
        *tx = set_result_get_publicKey();
        THROW(0x9000);
    }
    else {
        display_address_confirmation_ui(
                address,
                on_address_confirmed,
                on_address_rejected
        );

        *flags |= IO_ASYNCH_REPLY;
    }
}

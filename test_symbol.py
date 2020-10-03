#!/usr/bin/env python
# *******************************************************************************
# *   Ledger Blue
# *   (c) 2020 Ledger
# *   (c) 2020 FDS
# *
# *  Licensed under the Apache License, Version 2.0 (the "License");
# *  you may not use this file except in compliance with the License.
# *  You may obtain a copy of the License at
# *
# *      http://www.apache.org/licenses/LICENSE-2.0
# *
# *  Unless required by applicable law or agreed to in writing, software
# *  distributed under the License is distributed on an "AS IS" BASIS,
# *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# *  See the License for the specific language governing permissions and
# *  limitations under the License.
# ********************************************************************************
from ledgerblue.comm import getDongle
from ledgerblue.commException import CommException

bipp32_path = (
      "8000002C"
    + "800010F7"
    + "80000000"
    + "80000000"
    + "80000000")
test_net_network_type = "98"

dongle = getDongle(True)

# Get public key
publicKey = dongle.exchange(bytes(bytearray.fromhex("E00201801605" + bipp32_path + test_net_network_type)))
print("publicKey respond       [" + str(len(publicKey)) + "] " + publicKey.hex().upper())


# Note: P1_FIRST: 0x80, P1_MORE: 0x81; P1_LAST: 0x00
# transfer tx
transferTx = "E004008090058000002C800010F78000000080000000800000006C1B92391CCB41C96478471C2634C111D9E989DECD66130C0430B5B8D20117CD0198544180841E0000000000F6A98B390600000098F2A5E8E063AD1A9085EF5B5167E2F1A5645C48FA2C024917000100000000006008ADEC6BE7665B40A5AE0200000000005468697320697320612074657374206D657373616765"
transferTxNotXYM = "E004008090058000002C800010F78000000080000000800000006C1B92391CCB41C96478471C2634C111D9E989DECD66130C0430B5B8D20117CD0198544180841E0000000000F6A98B390600000098F2A5E8E063AD1A9085EF5B5167E2F1A5645C48FA2C024917000100000000001AB2C5CA0D99625E40A5AE0200000000005468697320697320612074657374206D657373616765"

createMosaic1 = "E0048081FF058000002C800010F78000000080000000800000006C1B92391CCB41C96478471C2634C111D9E989DECD66130C0430B5B8D20117CD0198414180841E0000000000F9BD913906000000E5F37FE3F83F4F0A2F21E7CF25F75CF29A20D7929CBEB7EB552EDA846969281F9000000000000000460000000000000017140D44583C4BAD44C0A9DB963E315E1C425A7495271738B8F81938DDE75C400000000001984D4171243F1123B82C530A00000000000000EADF0D4407000000410000000000000017140D44583C4BAD44C0A9DB963E315E1C425A7495271738B8F81938DDE75C400000000001984D4271243F1123B82C5340420F0000000000010000000000"
createMosaic2 = "E0040180020000"

createNamespace = "E00400806C058000002C800010F78000000080000000800000006C1B92391CCB41C96478471C2634C111D9E989DECD66130C0430B5B8D20117CD01984E4180841E00000000000985923906000000E803000000000000C880D8EBBA4A85A90011666F6F35373673676E6C78646E66626478"
createSubNamespace = "E00400806C058000002C800010F78000000080000000800000006C1B92391CCB41C96478471C2634C111D9E989DECD66130C0430B5B8D20117CD01984E4180841E00000000000985923906000000E803000000000000C880D8EBBA4A85A90111666F6F35373673676E6C78646E66626478"

supplyChangeMosaic = "E00400805A058000002C800010F78000000080000000800000006C1B92391CCB41C96478471C2634C111D9E989DECD66130C0430B5B8D20117CD01984D4280841E00000000001F2A933906000000CC403C7A113BDF7C40420F000000000001"

linkNamespaceToMosaic = "E00400805A058000002C800010F78000000080000000800000006C1B92391CCB41C96478471C2634C111D9E989DECD66130C0430B5B8D20117CD01984E4380841E00000000009B5096390600000054C07E58ACD1A982CC403C7A113BDF7C00"

linkNamespaceToAddress = "E00400806A058000002C800010F78000000080000000800000006C1B92391CCB41C96478471C2634C111D9E989DECD66130C0430B5B8D20117CD01984E4280841E0000000000A92B97390600000054C07E58ACD1A98298F2A5E8E063AD1A9085EF5B5167E2F1A5645C48FA2C024901"

accountMultisig = "E0040080D9058000002C800010F78000000080000000800000006C1B92391CCB41C96478471C2634C111D9E989DECD66130C0430B5B8D20117CD0198414280841E000000000077769F5906000000043D6F6E851CAE4ED2B975AEEF61DFDF00B85BBB2503AC23DD7586E3C0B079566800000000000000680000000000000017140D44583C4BAD44C0A9DB963E315E1C425A7495271738B8F81938DDE75C40000000000198554101010200000000009817259A942F6AE0EA32B01E368687405536E61125ECF701984B730EA3B726CC12A9FAF78B4D37354FF8722DBB950137"
hashLockAccountMultisig = "E004008081058000002C800010F78000000080000000000000006C1B92391CCB41C96478471C2634C111D9E989DECD66130C0430B5B8D20117CD0198484180841E0000000000D58B993906000000A84582052890A9518096980000000000E0010000000000002B51EBCBC3E40EFE8AF68A0408F5A72474B1327A64E3E3B47D9B139230C7833B"

multisigTransaferTx = "E0040080E1058000002C800010F78000000080000000800000006C1B92391CCB41C96478471C2634C111D9E989DECD66130C0430B5B8D20117CD019841422076000000000000E73BE96B060000004941C270B56778E01629FC82EDDC622668F076CE1583AFCCA3F6DE7FE03615BB70000000000000006D000000000000007299D0308AA442C6EB7885B74BD7049A8B2236E6A3E0CC6FDD4036F543A3C6E40000000001985441985507CA7F3D1C9069E16E1A0FCE7C5AD4607421ED31E6730D000100000000006008ADEC6BE7665B80969800000000000054657374206D657373616765000000"

multisigCreateMosaic1 = "E0048081FF058000002C800010F78000000080000000800000006C1B92391CCB41C96478471C2634C111D9E989DECD66130C0430B5B8D20117CD01984142A0830000000000007C0FED6B06000000705B456E99A2FA7DA3D4F02ABB1993774426B8095705C2116E6FB59E95A2587D900000000000000046000000000000007299D0308AA442C6EB7885B74BD7049A8B2236E6A3E0CC6FDD4036F543A3C6E40000000001984D41645AC697472FCA780000000000000000E65EF6F70300000041000000000000007299D0308AA442C6EB7885B74BD7049A8B2236E6A3E0CC6FDD4036F543A3C6E40000000001984D42645AC697472FCA780065CD1D00000000010000000000"
multisigCreateMosaic2 = "E0040180020000"

multisigCreateNamespace = "E0040080C1058000002C800010F78000000080000000800000006C1B92391CCB41C96478471C2634C111D9E989DECD66130C0430B5B8D20117CD01984142A0680000000000006A87F06B06000000B96E1C08F8434BFDC4D1F292EB3F911B1A3C5B3EE102887A8ACDD75A79A4BB6250000000000000004A000000000000007299D0308AA442C6EB7885B74BD7049A8B2236E6A3E0CC6FDD4036F543A3C6E40000000001984E4100A30200000000004F870552748FEBB000086D756C7469736967000000000000"
hashLockMultisigCreateNamespace = "E004008081058000002C800010F78000000080000000800000006C1B92391CCB41C96478471C2634C111D9E989DECD66130C0430B5B8D20117CD01984841A04D00000000000052C3F06B060000006008ADEC6BE7665B8096980000000000E803000000000000E019A4A92002505B8B5029AE556958ADCDFBEDAC26C2F79DE1668C5BC588EDF7"
multisigCreateSubNamespace = "E004008071058000002C800010F78000000080000000800000006C1B92391CCB41C96478471C2634C111D9E989DECD66130C0430B5B8D20117CD01984E41E0460000000000005632F36B060000001409CC7609AC4FD6952019898F84F5A401167375625F6E616D6573706163655F6D756C7469736967"
txCosignature = "E004008171058000002C800010F780000000800000008000000089F54478AD080E36912701C20DDE49B13A5E8702953C68EA24F5EE2EF068AE0A01984142C0C8030000000000BD358D8C0600000000000000000000000000000000000000000000000000000000000000000000000000000000000000"

transferTxRespode = dongle.exchange(bytes(bytearray.fromhex(transferTx)))
transferTxNotXYMRespode = dongle.exchange(bytes(bytearray.fromhex(transferTxNotXYM)))

## 2 transactions needed for mosaic creation and mosaic supply change transaction
# createMosaicRespode = dongle.exchange(bytes(bytearray.fromhex(createMosaic1)))
# createMosaicRespode2 = dongle.exchange(bytes(bytearray.fromhex(createMosaic2)))

# createNamespaceRespode = dongle.exchange(bytes(bytearray.fromhex(createNamespace)))
# createSubNamespaceRespode = dongle.exchange(bytes(bytearray.fromhex(createSubNamespace)))
# supplyChangeMosaicRespode = dongle.exchange(bytes(bytearray.fromhex(supplyChangeMosaic)))
# linkNamespaceToMosaicTxRespode = dongle.exchange(bytes(bytearray.fromhex(linkNamespaceToMosaic)))
# linkNamespaceToAdresssRespode = dongle.exchange(bytes(bytearray.fromhex(linkNamespaceToAddress)))
# accountMultisig = dongle.exchange(bytes(bytearray.fromhex(accountMultisig)))
# hashLockAccountMultisig = dongle.exchange(bytes(bytearray.fromhex(hashLockAccountMultisig)))
# multisigTransaferTxRespode = dongle.exchange(bytes(bytearray.fromhex(multisigTransaferTx)))
# multisigCreateMosaic1Respode = dongle.exchange(bytes(bytearray.fromhex(multisigCreateMosaic1)))
# multisigCreateMosaic2Respode = dongle.exchange(bytes(bytearray.fromhex(multisigCreateMosaic2)))
# multisigCreateNamespaceRespode = dongle.exchange(bytes(bytearray.fromhex(multisigCreateNamespace)))
# hashLockMultisigCreateNamespaceRespode = dongle.exchange(bytes(bytearray.fromhex(hashLockMultisigCreateNamespace)))
# multisigCreateSubNamespaceRespode = dongle.exchange(bytes(bytearray.fromhex(multisigCreateSubNamespace)))
# txCosignatureRespode = dongle.exchange(bytes(bytearray.fromhex(txCosignature)))

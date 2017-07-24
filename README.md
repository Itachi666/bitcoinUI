1.1 create funding transaction
[fundingtx],txidfundingtx,redeemscripta,fundingtx_1,fundingtx_2,fundingtx_3 = createfundingtx(pre_txid1,voutx1,pre_txid2,voutx2,z,ha,pkb,pkam,nsequence)
1.2 create commitment transaction
[commitmenttx],txidcommitmenttx,redeemscriptb,commitmenttx_1,commitmenttx_2 = createcommitmenttx(txidfundingtx,0,z,pkam,h,pka,pkbm,nsequence)
1.3 create timeout commitment transaction
[timeoutcommmitmenttx],txidtimeoutcommmitmenttx,timeoutcommmitmenttx_1,timeoutcommmitmenttx_2 = createone2onetx(txidfundingtx,0,z,pkb)
1.4 create delivery tramsaction
[deliverytx],txiddeliverytx,deliverytx_1,deliverytx_2 = createone2onetx(txidtimeoutcommmitmenttx,1,z,pkbm)
1.5 create timeout delivery transaction
[timeoutdeliverytx],txidtimeoutdeliverytx,timeoutdeliverytx_1,timeoutdeliverytx_2 = createone2onetx(txidtimeoutcommmitmenttx,1,z,pka)



2.1 sign funding transaction
[sign_fundingtransaction],[siga],[sigb] = sign_fundingtransaction(fundingtx_1,fundingtx_2,fundingtx_3,pka,ska,pkb,skb)
2.2 sign commitment transaction
sign_commitmenttransaction,sigam,[sigb1] = sign_commitmenttransaction(commitmenttx_1,commitmenttx_2,ska,skb,redeemscripta,ha)
2.3 sign timeout commitment transaction
[sign_timeoutcommitmenttransaction],[sigb2] = sign_timeoutcommitmenttransaction(one2onetx_1,one2onetx_2,skb,redeemscripta,ha1)
2.4 sign delivery transaction
sign_deliverytransaction,[siga1],sigbm = sign_deliverytransaction(one2onetx_1,one2onetx_2,ska,skb,redeemscriptb,hb)
2.5 sign timeoutdelivery transaction
[sign_timeoutdeliverytransaction],[siga2] = sign_timeoutdeliverytransaction(one2onetx_1,one2onetx_2,ska,redeemscriptb,hb1)




3.1 send funding transaction
nothing
3.2 send commitment transaction
[sign_commitmenttransaction],[sigam]
3.3 send timeout commitment transaction
nothing
3.4 send delivery transaction
[sign_deliverytransaction],[sigbm]
3.5 send timeoutdelivery transaction
nothing







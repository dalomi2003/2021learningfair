count_E = 0
count_I = 0

count_S = 0
count_N = 0

count_T = 0
count_F = 0

count_J = 0
count_P = 0
while True:
    answer = input('''Q1. 오늘은 1교시 전공 첫 대면 수업에 가는 날!
    1. 아는 친구를 찾아보고 만나서 같이 가려고 한다.
    2. 혼자 할 일만 후딱 하고 나와야겠다고 생각한다.
    ''')

    if answer == '1':
        count_E += 1
        break
    elif answer == '2':
        count_I += 1
        break
    else:
        print("잘못 입력")
        continue

while True:
    answer = input('''Q2. 수업 시작까지 한 시간이 남았고, 아직 나갈 준비를 하지 않았다.
    1. 늦을 수도 있겠다며 분주하게 움직인다.
    2. 아 피곤한데... 조금만 있다가 슬슬 준비해야겠다고 생각한다.
    ''')

    if answer == '1':
        count_J += 1
        break
    elif answer == '2':
        count_P += 1
        break
    else:
        print("잘못 입력")
        continue

while True:
    answer = input('''Q3. 디대 건물에 들어갔더니 바닥이 빗물에 젖어 너무 미끄럽다!
    1. 다들 제대로 안 닦고 들어왔나... 조심해야겠네.
    2.  와 들어가다 여기서 넘어지면 첫날부터 유명해지겠는데?
    ''')

    if answer == '1':
        count_S += 1
        break
    elif answer == '2':
        count_N += 1
        break
    else:
        print("잘못 입력")
        continue

while True:
    answer = input('''Q4. 강의실에 도착했는데 교수님이 안 오셔서 멀뚱히 앉아 있다. 그때 옆자리의 처음 보는 학생이 교수님이 조금 늦는다고 하셨다며 나에 대해서도 자연스레 물어보기 시작한다.
    1. 오 감사해요! (이분이랑 친해지면 되겠다!)
    2. 감사합니다, 근데 너무 어색하다...
    ''')

    if answer == '1':
        count_E += 1
        break
    elif answer == '2':
        count_I += 1
        break
    else:
        print("잘못 입력")
        continue

while True:
    answer = input('''Q5. 늦은 교수님이 들어오면서 하길 원하는 말은?
    1. 수업 때 사용할 컴퓨터 때문에 사무실에 볼 일이 생겨서 해결하느라 시간이 조금 걸렸습니다. 죄송합니다. 바로 시작할게요!
    2. 첫 수업부터 기다리게 해서 정말 죄송해요... 안 그래도 어색한데, 가만히 있느라 더 뻘쭘하셨겠다. 이제 수업 시작해볼까요?
    ''')

    if answer == '1':
        count_T += 1
        break
    elif answer == '2':
        count_F += 1
        break
    else:
        print("잘못 입력")
        continue

while True:
    answer = input('''Q6. 수업 중 자기소개를 하게 됐다!
    1. 역시 사람 앞에 두고 말로 설명하는 게 더 자연스럽고 편해!
    2. 아, 비대면으로 했으면 더 나았을 텐데... 약간 후회한다.
    ''')

    if answer == '1':
        count_E += 1
        break
    elif answer == '2':
        count_I += 1
        break
    else:
        print("잘못 입력")
        continue

while True:
    answer = input('''Q7. 수업이 끝나고 사야 할 재료가 생겨 화방으로 갔더니, 처음 보는 다양한 재료가 많이 쌓여있다.
    1. 필요할 것 같다고 생각한 종류의 재료 위주로 찾게 된다.
    2. 평소 내 취향의 색감인 멋진 재료나 처음 보는 도구에 더 관심이 간다.
    ''')

    if answer == '1':
        count_S += 1
        break
    elif answer == '2':
        count_N += 1
        break
    else:
        print("잘못 입력")
        continue

while True:
    answer = input('''Q8. 이제 화방에서 구매를 하려고 한다.
    1. 원래 사려고 했던 것만 계산대에 올린다.
    2. 오 이것도 있으면 좋겠는데? 몇 개를 더 추가한다.
    ''')

    if answer == '1':
        count_J += 1
        break
    elif answer == '2':
        count_P += 1
        break
    else:
        print("잘못 입력")
        continue

while True:
    answer = input('''Q9. 화방을 나가면서 당신은?
    1. 책 빌릴 것도 있으니 이제 도서관 들러야겠다. 밖에서 해야 할 일들을 정리한다.
    2. 휴, 이제 수업 다 끝났네. 일단 나가자!
    ''')

    if answer == '1':
        count_J += 1
        break
    elif answer == '2':
        count_P += 1
        break
    else:
        print("잘못 입력")
        continue

while True:
    answer = input('''Q10. 디대 건물을 나오던 중 쓰레기통 앞에 버려진 커다란 실기 작품을 발견했다.
    1.  너무 커서 못 넣은 건가? 근데 저렇게 두고 가도 되나?
    2. 헐 잘했는데 왜... 버릴 때 아까웠겠다.
    ''')

    if answer == '1':
        count_T += 1
        break
    elif answer == '2':
        count_F += 1
        break
    else:
        print("잘못 입력")
        continue

while True:
    answer = input('''Q11. 다음날, 나의 디자인 계획에 대해 발표해야 한다!
    1. 참고한 자료는 어떤 것인지, 제작 과정을 어떻게 나눌지부터 설명한다.
    2. 다양한 사진 자료를 보여준 후 본인이 표현하고자 하는 이미지와 전달하려는 메시지를 설명하는 데 집중한다.
    ''')

    if answer == '1':
        count_S += 1
        break
    elif answer == '2':
        count_N += 1
        break
    else:
        print("잘못 입력")
        continue


while True:
    answer = input('''Q12. 발표 후 주변에서 칭찬을 받는다면 듣고 싶은 말은?
    1.  와 이거 어렵고 시간도 부족했을 텐데 어떻게 이만큼 하셨어요? 배우고 싶어요. 부럽네요. 
    2. 이거 하느라 진짜 수고하셨어요 ㅠㅠ OO 님이랑 같이 수업 들을 수 있어서 정말 좋아요. 역시!
    ''')

    if answer == '1':
        count_T += 1
        break
    elif answer == '2':
        count_F += 1
        break
    else:
        print("잘못 입력")
        continue

print("[ 결과 :", end="")
if count_E > count_I:
    print("E", end="")
else:
    print("I", end="")
    
if count_S > count_N:
    print("S", end="")
else:
    print("N", end="")

if count_T > count_F:
    print("T", end="")
else:
    print("F", end="")

if count_J > count_P:
    print("J", end="")
else:
    print("P", end="")


a=input('당신의 mbti를 적어주세요! :')

intp ='''INTP 연필
당신은 디대생의 필수품, 연필 같은 사람!
관심 있는 것이 생기면 먼저 논리적인 분석에 들어가기 시작합니다.
추상적이기만 한 것에 그치지 않고, 눈앞에 자신의 아이디어가 바로바로 보이도록 스케치가 나와야 직성이 풀리죠.
얌전해 보이지만 어디서나 쉽게 스며들곤 합니다. 필통이든 연필꽂이든, 언제나 자신을 위한 자리가 있다는 듯 말이에요.
관심 분야에서만큼은 문제 해결에 높은 집중력을 보이며 늘 분석적인 당신은, 종종 회의적이거나 비판적인 시선을 갖기도
하지만 뛰어난 해결력을 가지고 있어 누구에게나 필요한 존재가 되곤 합니다.
                                                                                                    
     .Y:                                                                                            
      YgBBBSv:.                                                                                     
         rgBBBQBB2::...                                                                             
            rEBBP::::::irii::..                                                                     
               77i::::.::::iiiirii::::..                                                            
                 .iii::::.:::.:::::::::irrrrr:.                                                     
                    .rrr::::.:::::::::::rrrri7r7ri.                                                 
                      .:7rr::::::::.:::::.iiiiiirr7r7:.                                             
                         :i7riii::::::....ii:i:iiiiiir:qQSr.                                        
                            :r7ii:::::::iiii::i:i:i:i:rBBBgQBQ1:                                    
                              .:rrii::ir:i:iiiii:i:::.jBBBQRQQBBEbU2i                               
                                 .irri:iiiiii:iii:::..qE7ZQRBQBQBBBBBBQ7                            
                                    .riv77rriiiiii:.iXQ5:g:grgXgMQERMgBBBQ15r:                      
                                       .:i7vvrrii::rQBBMBDEP:P KqjggQRBQBQBRBBQI7:                  
                                           .:i7v7r:MBBBBBBBMQPXBvIgEgBJbBBBBQQMBQBS.                
                                                :iXBBQBBBBBQBQBB2dEKRr sruJLb5BBBB55PUs:.           
                                                   :r1dQBBBBQBBgdZKqQILR.7:D:rX7qZv52XPZEbui        
                                                        ivdMBBBQBBBBBBBQBIXBBBD. 7IU2ISSqqZgq       
                                                            :2BBBBBBQBBBBQ..QBR5rU2UU5252S5qP1      
                                                                ruKZBBBBBBQgBBBdJI52IUI1U1I2SK      
                                                                    .iLPRgQBBBBK2KSqKXI5222IK5      
                                                                        .:vqBBQDZPPqdqqXqKXSE.      
                                                                              .L5DRQggZDbbEgi       
                                                                                  .i2ZQQQE5.        
                                                                                       ..           
'''
if a == 'intp' or a == 'INTP':
      print(intp)

esfj ='''ESFJ 마우스
당신은 짝꿍이 있다면 만능, 마우스 같은 사람!
컴퓨터와 연결되면 찰떡같이 행동을 옮겨주듯, 매사에 협조적이며 따뜻한 모습을 보여줍니다.
늘 그 자리에서 조화를 만들어내며, 목표를 위한 결정권을 가집니다.
제 할 일에 정확한 것은 물론 다른 사람과 함께 일하는 것을 좋아하죠.
그래서 남들처럼 팀플 소식에 몸서리치기보단 기대와 설렘을 느끼는 경우가 많습니다.
사소한 일까지 성실히 해내는 당신은, 다른 사람들이 필요로 하는 것을 잘 알아차리며 그 노력이 인정받는 것을 무척이나 좋아합니다.
                                                                                                                           
                                     .r1qMQBBBBBBBBBQBMZ27:                     
                                 .vKMRRDEPPKPPEZggQQQQBBBBBBBDJ.                
                              .JEQgb5Iu1J1suu2IKqPbDZggMMQMQQBBBBEi             
                           .JZQDP22jjsJLL71LJuUUKXbbZEZEgZgDMDgMBBBBI           
                        .JDQgPU1uussYY77vdB1vI1SSKqdbEEDZgZgZgZgDMgBBBI         
                      LZBMPI2uuJjYYv771bgS1UI25IXXPPddZdZZgDgDgDgZgZMQBBi       
                   rPBRP11JsvYvv7v772gEIsjuUUI2XSqPEdZZDZgDgZgZDEgZMgQQBQU      
                 1BBZ2Jvv7vrr:rs5YIgqLLJ1u21I255qqddZZgDgDgDgZgMQBBQBBBQBBU     
              .DBBKJ7v77rr:ivdBQSZq:.juUuU1I2SSqKddDZgZgDgZRQBQQdSI2u5PRBBB:    
            :QBRXsY777ri:rPBBBb1P7..vUUUI2IUXXPPddgDgDgZRQBRZ5srrii::..:JgBq    
          .BBQIULvrrrr:JBBQBgDgP..:J55U2U55KXPPZEDEDZgMBQE2J7v77ri::...:.iBg..  
        .gBQSjjL7r7rrYQMv     v1:rISSUI25SqKbbZZgZDZMBQP1LYvvri::.:ir7sYJuBLi.  
       KBB21js7vrrirED.  .::.7YrvXKS252XXPPddDEDZgDQQE1jssr::irsUPdgggbdEB5ri:  
     iBBXJuLL77rr:vQv  :rriiIqsuqXXIS5KKPPddDZgZggBgKu1Yr::7qgQRQggDgEggBZ7r:.  
    SBMjsJvv77rr:jBi .i77rYgPUIPXX5XSqqdPEbZEgDgMQPIUur:iIgBQMgMgMgMgRMBMvri.   
   RBKYLv7v7777:UBs :r77LPgI2Xq5KSqXqKPPEEZEDZgQRXI1Y:rXQQRgMgMgQRQMQQBQvri.    
  MBq77v7v7LvvrsQB .r71KbPUXSKSKSqKPPdbEdDEDDgRDI51r:2QQgMDMMQRQQQQBBBZvr:.     
 ugK7r77v7vvLv7RBP :vUP552K5XSKXPqbPEPZEDEgZgQZ5SY:rQBMgMgRRQQQQBQBBQ17r:       
 BU1ir7v7YLYLL7qDPirs21IIK5XXqKPPbbEdZdDEDZRRd557:uBRMgMMQQBQQBBQBDUrr:.        
.BPLj7YYJYjYJv1dSYUIKIXI55XSqKbPEdZEZEDEgDQQPS2riPBMggMRQQBBBBBQqvr:.           
 bQX1UsJJuJJv5DSIKqX5SIX5KXqqbbZbZEDZDEgZQMPS1ivRBgMgQMQQBBBBZsr:..             
  BBES21jsuLqZSSK5SIX5KSqXPPdPZdZEDEgZDgQgPSYiUQQgMgQQBBBBDur:.                 
   BBQbK52uqdqXqXKSSXKXKKPPdbZdDZZEgDZgBDPIvrZQQDRMBQBBRUr:.                    
    BBBREqPZPKq5qSqSqXPKPqbbEEgEDZgZMQBgPU7sQQMgRQBQBXv:.                       
     YBBBQDbqdPPqqSKKqKPqbPZEEZDEDgQRBEKuLqBQMgQBBDUi.                          
       KBBBBQZEdbPbPPqPqbPdEEbZDMQQRQgXJSMBQQRBQZv:.                            
        .EQBBBQQgDEEEDEggMDggQQQQQRQgXSDQBRQBBP7..                              
          .vBQBBBBBgRQBQBQQQQQQRQRQQgZQQQBBBdr.                                 
             LMBBBBBQBQBQQQQQQQQQQMRgQQBBBP7.                                   
               .ugBQBBBBBQQQQRQRRgRRBBBBgr.                                     
                  .7KBBBBBQBBBQBBBQBQBSi                                        
                      .rIEBQBBBBBBBXr                                           
                            .:::.                                               
                                                                                
                                                                                
                                                                                
                                                                                
         
'''
if a == 'esfj' or a == 'ESFJ':
      print(esfj)

istp ='''ISTP 커터칼
당신은 날카로운 커터칼 같은 사람!
웬만한 건 다 자를 수 있을 만큼 날카로워서, 뭘 자를지 포착만 한다면 철두철미한 해결력을 보여줍니다.
문제의 원인과 결과까지 논리적으로 척척 파악하고, 마주한 과제의 핵심을 분리하기 위해 수많은 양의 자료를 찾는 일도 소화해냅니다.
합리적이고 효율적인 것을 중시하며 장인 정신까지 발휘할 줄 아는 당신은, 날카로운 객관적 판단과 최소한의 고생으로 완성도 높은 결과물을 만들어내는 능력이 있습니다.
                                                                                                    
          .:::iii.:::..                                                                             
        .i::.::.:i...:...:iJvs7:..                                                                  
      ......:.. ..ii::i:i:...:RKS2UYvr:..                                                           
    :5u7::..   ...    ...:::::rYj2U52512Jsv7ri:.                                                    
   .ii7vjuUYvr:i.    ..     .   ..:ivs25K5I22jjssLv7r::                                             
         ..irvY117:.                   ..irsUSSK5IjJvLvv77ii:.                                      
              .:YIEgDK1r:   .                 .:rvUU1Juvs7rirr777i:.                                
                 ..:i7YSQBgKSIJYri:..               .: 7BBBBg5sLrrr7r7rr::                          
                      .ivjbPq551U1UuuLLri:.         BB 7BBBBBBBBBRE5uvrirrLvvri:.                   
                       .:ii7L12SSX5IjjJuj1uuv7r:..  .. BBBQBIK9999999BMBQvr7777Lvvrr.               
                            ..:i7vuUSSXI2JJYsYJu1JJ7: rQQBBQBBQZP1jJPgBBBPgdKuLr7r7rZBPr            
                                 ..::r7Jj55K22jJvvvLvLr:::iv1PgBBBQBMDQBBIi2EQQQMgqjBBBBQg          
                                      ..::r7LuI2SU2jjvvrrii::.::i715ERBBB      .iv5qRQBQQQB:        
                                            ..:irvJ225IIjJvvrrrrii:i:::r.              d1r1Bi       
                                                  .:ir7LuUSIIuj77rrrYr1iY2vuYii..      PX751B.      
                                                       ..:i7vU1IUurir:irisrKvIKYLLPM57qXrLJrQB      
                                                            .:irY152Jr7i:r.ir:s7S75qUQBdsI7LrQ:     
                                                               ..irsuI2UJLr7i:7:r7iL:r7USDEMqBB     
                                                                  ..:rvj22SUUjYrvi:r7ri:::iruEB     
                                                                      ..:irvsU2S221jLY77rri:::v.    
                                                                           ..:ir7Luu5UI2I1usYLX.    
                                                                                 ...:ii7vJJ2IX7     
                                                                                         ..:.       
                                                                                                    
'''
if a == 'istp' or a == 'ISTP':
      print(istp)


enfj ='''ENFJ 셀로판지
당신은 알록달록하며 조금은 투명한, 셀로판지 같은 사람! 
서로 간의 결합으로 새로운 색을 만들어내는 셀로판지처럼, 타인의 욕구와 잠재력을 금방 파악함과 동시에 그것을 최대한 발휘시키는 능력이 있습니다.
모두가 누구와도 잘 섞일 수 있게 만드는 평화주의적 마인드의 당신은, 뛰어난 리더로서의 면모를 보여주기도 하죠.
하지만 그만큼 다른 이에게 영향을 받는다는 특성 때문에 주변에서 들리는 자신의 평가에 대해 조금 민감한 편입니다.
                               ... ..:.:....                                                        
                                 .is..::::::::::::::.....                                           
                              .sKDgBj ...:::.:.:.::::::i:iii::::.. r7.                              
                          :YPDQBMdPPM: ...:...:.:.:.:.:.:::::::::.7Dgd5i                            
                     .iUPMggPqqDdEEZMg. .........:.:.:.:.:.:.:.. rqS1IXEb1:                         
                 :v5gggPP525X2KqPqbPZgS ....:.:.:.:.:.:.:.:.:.. rqIu1JUuIKZPu:                      
            .iubgMZbKS2IUS15IUXqSqXPKbQ7 ....:.:::::::.:.:.:.. rqIu1JuJ1uU15qDPY.                   
        :7KZRDZPP5IUIU2152I15UPXXXKXqKDR: ....:.:::::::::::.. rqSuUjusjsjjjJ115PZX7.                
   .iUPRMgbPXK5SI5UU12122S12UIDP5qSKXqKMq  ....:.:.:.:::::.. 7P5XI12jUJuJ1J1Juu1UKPDK7              
rPRRMZbKK5X252I2I12u212U2252USD5PKqXKSKKQv .......:.:::.:.. 7EXJX55I5I52511u1j1u1uUuSdDIr           
 IBdXS5S2S25UIUI111211j1uI1IuqPqbq5S5XSqqR: .....:.:.:.:.. rdXI2UI1I25IXIX55UI2511uIU22qED1i        
  DZKISI525UI2IUI1UU2u1j21UuUIK5SIS5SIS5XbZ ....:...:.... rb51U1Uu2jujUj2UI2SIXI21X5I222I2bDEs:     
   QqS2I25II222IU212u1uU1I1UJ55S2SISIX5SIXD1 ......:.:.. rP5uUuUuUuuJ1J1juu1j11U1U25IS5K5SS5KDMZv.  
   iQKSI52I2IU522u1j1u1u2UIuuISISI5ISISI5IKgi ....:.:.. rPS11J1j1j2juJujuJUu1u1jUuU1U1IU5ISUKSKPRBB.
    ug55UIUI2U1Iu1JUjuju12uujS2S2S25I5ISISIPE. ....... rqIu1J1j1u1j1JuJuJujUj1jUJ1uUuU1Uu2U2UI2XPBX 
     PZ5525UI121Uu1j1JujUj1JU2IUIU5II2I252S2E2  ..... 7PIu1juj1JuuususuJuJuJ1j1u1u1uUuU1U1UU21I5Rs  
      gb5522UIu2u1s1juJ1jujJu52IUIU52I22UI1ISgr    . rP2j1J1JuJjJ1JjJusjsuJ1J1u1j1uUjU1U11uUUISMv   
      :MK2I2511juJuuUJ1uuJus2U2UIU2121212u12XUM. :  :2svsYJsJu1sjsjsU11suJjsjjUj1J1uUu2uU1Uu25R7    
       jDS2IUuJ1uUuuj1JuJusJjUu1jjJusJYJYsL2SjZqdBBQMESUYY777YLssJLJY1u1JuJus1J1j1juuU1ujU12SMr     
        PbSU1JJYJsJLYvYvYvvvuJuu1u2U5SXqZbZEQZQQBQBQBMQMQgEKSujsjv7vYLJYjsusuJusuJ1uuuujU125gr      
         gqIJjJusjsuJ2U5SqKdZDdDZDZMgggMDDPMQRMQQQQQQBQMZgQBBQQBgK1J777v7LvssusuJujuuuuUuI5Mi       
         :RSUj5EEbEbZDDDgEEEgdDZgZgMRggPddgRQMQQQRMgRQBBBQBQBRggBQBQQEPIUsL7vvLvssujuj1u25g:        
          vD21ugDZbbPPPdPdqZgggQMQRMZDdgMQQQRgZRQQRQMQQBQQQQQBQMEEdZQBZggMDZbq2uYYvYs1j2Xg:         
           Xb1sqDPdPPPbPdPPPgMRgRDgDgRRZDEEPDZRgRQBRQQQRMgRgQRBQRRgKQgPPQggZggRggddPUJ2XZ.          
            ZKYXEbPPKEDMPDZZdDEddZbEqPqPqddZqgQRgQRQRQRRggdgMQgdPZDDMRPdQQgMPEdDDMRQJuXZ.           
            :gI1DbbKPbDZPEMZgEDZgZEKPPZEDPqJuEbdRQBQBQRgQDEDRQg5QgqbRQMgQRMggbdbZdQ2sKE.            
             LduPZPbPgDZKdDgZgDMgRQgZEXIL7riIRERQgRBQBEgMQEgQQdqMgqPbQRRgQgQRQDZPgDYSE              
              5SPdbPbPggPqDMMRQQQgbUJ7rr7rr7MZEZMdQQQQMZDDEZQdqqDPdqPZRddgQgMRMMDQ5IP               
               PPgPPqPPDdZZQMDS177rr7vvLLLrPRDDBQBQBQBggDgEQdPKbdbPZgQdPMQRRdMZgQRXP                
               .ggZdZDgEdK2vvrrr77LvLLJLs7LQBgQRDQBQBBREgMQgDdPgZPgRQMgEMDMRQgMgBDP                 
                rBRgbXjLrrirrLvLvLvYvYssv7PBDZgggQQBQBQDDggbEZDMEZEMgMQQgRRQRQRBBX                  
                 2Kv7rrr77v777YYYvYLsYjYvYBQQgRQQRBQBQBDDgDbDEDdZEgZgDggRgQQQQBBd                   
                 .Jv7vvv7vvv77rvLsLsLJJs7gBQQQMRgQMQRBQRgRgMbZEDEZEZdggMDgggDRBQ                    
                  IYYvLvv7v7v777sLLvJYs7uBBRQMQRRMRMQRBQQZZdZdZEgEdbEbDDMDEqbMB                     
                  sUvL7v7v7Lvv77vJLsYsL7ZBRQRQRQRQMRMQQQZEbEdDdZEgbZEgDRMRMRMBI                     
                  7UsvLvv7v7777rvLsYJYLsBQQRQMQMQRRMQgBRdbZEDZDEggDdgDgZDdDERB                      
                  :XLvvv7v777777vYvsYY7DBQRQQQQQRQgQRQQMbZdZdgEgZgdEbdPbPdPZBI                      
                   IsvLvvr77v77rv7vvs7uBBRQQQQQRQQQMRQBggZDZgDgEDEDdZbEdZbDMB                       
                   1Jv7v7777777vrrrvLvdBQQQQQQMQQQMRMRRBQgPDZgEDDgEgZZdDdEZBJ                       
                   7Uvv7v777777v7r77LjBBBQBQQRQRQQQQQRQQBMZPDZDZgDgDgEZbEdQB                        
                   :IYvv7v77r7rvrrrvYUPggBBBBBBBBBBBQBQBQQMDZgZDZgZgZDEDbgBs                        
                   .5Lv777v77r777rrrUuU2XPMQBBBBBBBBBBBBBQQQQRQMgZDdgZgZgRB                         
                    uj7vvLvLvYvussssSbPZPq2u7r:.. .r1ZBBBBBBBBBBQRgMZZdDgBv                         
                    jK2u1sY77ii::..                     .i1bBBBBBBBBBgMgBB                          
                    .:                                         :vbQBBBBBBL                          
                                                                     .rXQ     
'''
if a == 'enfj' or a == 'ENFJ':
      print(enfj)

intj ='''INTJ 프린터
당신은 늘 다양한 그림을 생각하는 프린터 같은 사람!
독창적이고 다양한 아이디어를 떠올리고 실현하는 것에 큰 욕구가 있습니다. 프로젝트의 흐름을 빠르게 파악할 줄 알며, 프린터가 광범위한 인쇄물도 잘 출력하는 것처럼,
포괄적이고 광범위한 자신만의 전망에 따라 계획을 수행하죠. 하지만 그만큼 자신과 타인에 대해 높은 기준을 가진 당신은,
자칫 회의적이거나 독단적으로 보이긴 해도 부드러운 마음씨를 가지고 있습니다.                                                                                                    
                .:irrX7XXX7X77r;:,                                                                  
          :r2Z@aXZ00BBWWWWWWWW@WWB0ZaXr.                                                            
         ,MMMMMZ                     .., .MB                                                        
          BMWB@M.                     .   XM2                                                       
          r@M0WMZ          .   .   .   .   MM.                                                      
           BMBBWM       . . . . . . . . .  ,M@                                                      
           X@@8WM2           . . . . . . .  ZMi                                                     
            WM00WM                  .   .    MM                                                     
            X@W8WMa                          XMX                ......                              
            ;WW8WW@           ....,.:,::ii;;;;888ZZaa2a2a22S2XSZ00B0WWBZi                           
       7XXXa8B00ZS;rr77X7XXSXSXSSSXSS2SSS2aZZaXXX22aaaaZaZZZZ8ZZZZZZZZZ0BZSXr;:.                    
      X22XX777XXSX7r77XXXXXXXXXXXXXXXXSXSS222S2Sa2a2aaaaZaZaZZZZZaZZZaZaZ8BB@@MWWB8aX:              
      ;aXXSSX7r77XXXXXXXXXXXXXXSXSS2S2S22a2a2aaaaZaZaZZZZZZZZZZZZZZZZ8Z8800BBWW@W@@MWMMW0S,         
       ;aXX7XXSXX7XXXXXXSS2S222Sa2aaaaaaa2a2aaaaZaZZZZZZZZ8Z8Z8888880000B000B0B0B0B0080BW@M0S       
        .SXX77XSS2SX7X7XXXS2aZaaS2SSXSS2XSS2aZZZZ8Z8Z8Z8Z88888Z8ZZZZaa22SSXXXX7X7X7XXX;XXSSZB8      
         XS7X7X77XXSSSSXXXXXXSZZZaaaZZZZZZ8Z8ZZaZaaaa22S2XXXXrr;;ii:::::iiiir;77XXSXXSX7ZaZZWB      
         SZX7XXX7X7XXXS2SXXX7XXS2ZZZaZ22SSXX7777;;ii::::,,.,.,,::iirrXXSSSSa2aS2S22a2ZZ88080MX      
         XZ22X77X7XXX7XXXXSSSXXX7ir;;ii::::,,.,.,.,,:,ii;;rrXXXXSS2S2S2SSSSSSS2SaaZZZZ8ZZZ80M       
         Xa22aX77XXXXXXXXXXSXSXSS .,.,,:,:i;;r;r7X7XXXXSSSXSXSXXXXXX7XXXXSS22aaZZZZZaZZZZZ8@S       
         7ZS22a2X7XXXXXXXXXXXXSS2 ii;rXXSS222S2SSSSXSSSXXXXXXXXXSXSXSS2222a2ZaZaZaZaaaaaZZW@        
         7a2S22Z2XXXXXXXXXXXXXX2;:777X777777r77X7X7XXXXXXXXXXXXSSSXS2a222a22S2222a2ZZ88BBMM;        
         rZS2222ZXXXXXXXXXSXSXSS:rX7X7X7X7X7X7XXXXXXXXXXSXSXSXSSSSSXSXSXSSa2ZZ80BBWW@@@@MM7         
         ;a2S22aaS7XXSXSXXXSXS2r:X7X7X7X7X7X7X7XXXXXXXXXXXXX7777XXS2aZZ0BWW@@M@@WWW@WW@MM;          
         :ZS2Sa2ZS77XXXXXXSXSSS:r7X7X7X7XXXXX777X77r7r7r7X22aZ00WW@@M@M@@WWWWWWW@W@W@@MMi           
         ,a2S22a2aSXX7777XXXX2;i777777r7rr;rrrrXXSSaZ80BW@@M@M@@WWBWBBBWBWW@WWWWW@W@MMM             
         .ZS2S222ZB00ZZSX77rXr:;;;rr77XXSSaZ00BW@@@@@@@WWBBBBBBBBBBBWBWWWWWWWWWWWWMMM0              
         .aSS2S2S8000BBWBB08277S2Z800WWWWWBWWWBBBB0B0B0B0BBBBWBWWWBWW@@@WWWWWWWW@MMM7               
          aS2S2S280000B0BBWW@BWW@WWBWBWBWBBBBBB0BBBBBBBBWBWBWBWWWW@MMWWWM@MWW@MMMMB                 
          S2S2S2ZB000B0B0B0BBBBBBB0B0BBB0BBBBBBBBBBWBWBBBBBBBWW@BB8Z2X78@@@MMMMMMi                  
          Sa222SBBB0BBBBBBBBB0B0B0B0B0B0BBB0BBBBBBBBBBWBW@MMMMMM@WW08XS0WMMMM@2,                    
          aBZZZ0WWBBBBBBBBBB0BBB0B0B0B0BBBBBBBBBBWWW@MMMMMMMMMMMMMMMMWWM@2i                         
          aMB80BWBWBBBBBWBBBBBBBB0B0BBBBB0BBBB@@MMMMMMMMM@@@@W@W@W@@MMM@M2,                         
          .M@BWWBWBWBWBWBWBB8BBB0B0B0B0B0BBBBMMMMM@@WWWWW@WWW@@@@M@@@@@@MMMMMMBZBr                  
           ;MM@WWBWBWBWBWBWBBBBBBBB0B0BBBBW@MM@W@WWWW@@@MMM@M@@@M@M@@@M@MMM@MMMMMM:                 
            0MMM@WWWBWBWBWBBBBBBBBBBBBBWW@@MWWMMMMMM@@@M@M@M@@@@@M@M@@W@0Z0BWMMMa:                  
              70MMMM@WWBWBBBWBWBBBWW@@MMMW@@MMMMMMMMMMM@M@M@M@M@@WWB080BW8MMWa:                     
                 ;ZMMMMM@WWWW@MMMMMMMMM8XX7r;i  ,XBMMMMMMMW@BB00000WWM@@BZr.                        
                    .XBMMMMMMMMW0aXi.               :7ZMMMWBWB@@@WBZ2r,                             
                        ,XX;                            .S00a27i.           
'''
if a == 'intj' or a == 'INTJ':
      print(intj)

esfp ='''ESFP 스프레이
당신은 자유분방하며 붙임성 있는 스프레이 같은 사람!
즉흥적이지만 융통성 있고, 새로운 것에도 금세 적응합니다. 다정한 성격을 바탕으로 사람들과의 관계를 잘 챙기며,
그들과 함께 작업할 때 가장 즐거워하고 제 실력을 100% 발휘하죠. 매사에 주변을 밝게 만들려는 긍정적인 면이 있고,
썰렁한 분위기엔 질색하는 당신은, 타고난 순발력으로 현재 일어나는 일을 현실적 판단을 통해 헤쳐나가는 법을 잘 알고 있습니다.                                                                                                    
                                                .::i7:   . . .                                      
                                                ii::ir.   ::::::::::::::::::::::                      
                                              :uriii:7ur                                            
                                            .7PqL7UII5QgL.                                          
                                           :BBSsvsYL7rivKBi                                         
                                          .PPi....:     :jP                                         
                                         Qqjrri:.......::7UDB:                                      
                                         DBP7:::i2I5ddMgQQBBB                                       
                                         gBBdss7UBBBBBBBQBBBB                                       
                                         ZBBELsrYBBBBBBBBBBBB                                       
                                         Bd7i:.:uBv7KB:SQ:XLP                                       
                                         BZ:ii.rXQ 7Qrr:7rrLg                                       
                                         BDrr7:7JB:rri57r17jg                                       
                                         BDirr.:.bgQ.:XrrJ7LM                                       
                                         BQ ir.71B v.iiiY.vvg                                       
                                         RBbqrirJB1.EBiPBuBBB                                       
                                         QBBd77ivBBBBBBBBBBBB                                       
                                         RBBPr7iYBBBBBBBBQBQB                                       
                                         BBBPrri7BMREMPQBBBBB                                       
                                         BBBXrrirRXXPPPEBMRBB                                       
                                         KQgU77rsBQBRQZBQgbQB                                       
                                          .L7::i:PKP5jqjsvu..                                       
                                         QZ5r..: .:i  i:i71ZQ                                       
                                         QBQKrvrsBBQBBBBBBBBB                                       
                                         BB1ri:irDUSuuEBBBBBB                                       
                                         BBj7ir:iEP1jsuvDDPPB                                       
                                         BBJ7ii:rE5K1Kqu2KKBB                                       
                                         QBEJir:iq2u1BBBBBBBB                                       
                                         QQBS777sBBBQBBBBBBBB                                       
                                         qBBq..:iggEQgMdQQBBB                                       
                                         PBBXr...EZDEDEqQZURB                                       
                                         RBB5rrivBBQQgMbRi.vB                                       
                                         BBv.iivrBQQBBBZgUYQB                                       
                                         BBQ:.rr7BBQQdRQdRBBB                                       
                                         BBBd7L77BMQgs:UiPEBB                                       
                                         QBBPrLrvQBQBBjv1QBQB                                       
                                         QBBXi777QBBKqdq1QBBB                                       
                                         RBQPirirMBQqZRbBBBBB                                       
                                         BBBZ7:::BQrLJ2PBBBBBi                                      
                                         qBBB2qIqBBBBQBBBBBBB.                                      
                                             ..:iPgQQgq5Yr.                                         
                                                                 
'''
if a == 'esfp' or a == 'ESFP':
      print(esfp)

infj ='''INFJ 물레
당신은 든든한 도움이 되어주는 물레 같은 사람!
사람들이 하고자 하는 일과 그 동기를 잘 이해하는, 뛰어난 통찰력을 가졌습니다.
물레가 누군가의 손길에 힘을 실어주듯 사람들의 정신적 지도자가 될 수 있는 자질이 있으며,
자신의 비전을 체계적으로 구상할 줄 압니다. 사람들이 잘 모르는 내면에 자신만의 확고한 가치를 품고 있는 당신은,
마냥 얌전해 보이지만 가까워질수록 누군가에겐 없어선 안 될 존재가 됩니다.
                                    .,,::ii;i;;;;ri;iii:::..                                        
                             .::;;rrrrrrr;r;r;r;;;r;r;r;rrr;r;;ii:,                                 
                         ,:;;rrr;;;;i;i;i;i;i;i;i;i;i;i;iiiiiii;;;;rii,.                            
                    .:i;iii;i;i;iii;i;i;i;iiiiiii;i;i;iiiiiiii:iiii;;;;;i:.                        
                   i;r;;ii::::iiiii;iiiiiiiii;i;iiiii;iiiiiiiiii:iiiiiiii;;;ii.                     
               ,ir;;iiiiii:::::ii;iiiiiii;iii;i;i;i;iiiiiiii:i:i:iiiiiiiii:iii::.                  
              :;;;ii:i:iiiiiii:,,:iii;iii;iiiii;i;i;iii;ii:iiiii:iii:i:i:i::,::::ii,                
           ,i;iiii:iiiii:iiiii::,,:ii;iiiiiiiiiiiiiiiiiiiiiiiiii:i:i:i::,:::,::i:iii,              
           i;i:i:i:iii:i:i:i:iiiii,,.:i;iiiiiii;i;i;iiiiiiii:iii:i:i::,:,::::::i::,i:ii:            
         .;ii:i:::i:i:::i:i:iii:iii::..,ii;i;i;i;i;iiiiii:iiiiiii::,:,:,i::::::::,:,:::ii.          
        ,;:i:i:::i:::i:::::i:i:i:i:iii,..,i;iiiiiiiiiiiiiiiiii::,,,:,i::::,::::::::::::::;,         
       ,;:::i:::i:::::i:::i,:,::i:i:iiii: .:i;;iiiii;iiiiiii:,,,::::i::,:::,:,::,,:::,::::;i        
       ;:i:::::i:::::::::i:::::i,::::::iii,..i;;i;iiiiiii:,,.::i::::::::::::::::,:,:::,:::,;;       
      ;i:,:,:,i:::::::::i:::::i::i:,i:::::i::.,i;i;i;ii:,.,::::::::,:::,,::::,:,:,,::::,::,,;;      
     ,i:,:::,:::,:,:::,i::::::::::,::i::,:,::i,,:;;;:,,,,:::::,:,:::,:,:,:,:::,,,:,::i,:,:,:,X:     
     ii,:::::,i,:,::::ii:::,::::i:::::::::::::::,:i:,,:::::::,:,:,:,:,:,:,,,:::::,:,,,,,,,:,,:S     
     r,:::,:,i::,:,::::i,,,:::::i:::,:::::,:::::,ii,,:::::,:::::,:,:::,,,:,,,:,:,:,:,:::,:,:,.7;    
    .;:,:::,::i,:,,,:,:i:,:,:::,i::,:,:::,i::..:;;;i, :::,:,:,:,:,:::,:,,,:,:,,,,,,,:,:,,,:,,.iX    
    ,r.,,:,:,:i,,,,:,:,::,::,,,:,i::,:,iii,  :i;;;i;;: .:i,:,,,,,,,:,:,,,:,,,:,,,,,,,,,,,,,,,.,a.   
    ,r,,:,:,:,::,,,,,,:,i,,,:,,,,:i:iii:.  ,;;;i;i;i;;i  .i::,,,,,:,:,,,,.,.:.:.,,,,,,:.:,:,,.,Z:   
     X,,,,,,,,,i.:,:,,,:,:,,,:,::::;i:   :i;i;i;i;i;i;;;.  ,::,,,:,,,,,,,,.,,,.,,,,,.:,,,,.,,..Z.   
    X;.,.,,,,,,i,,,,,,.,.:,::::ii:    :;;;i;;;i;i;i;i;i;:  .:i::.,,,,:,:.,,,.,,,.,,,:..,,:,, iZ    
     ;S,.,,,,,,,::.,.,,,.,:iiiii,    ,i;i;;;i;i;i;;;i;i;;;i   .ii:.,.,.,,:,,.,,,,,.,,,.,,,,:. 7Z    
    .a7..,.,.,..,:.,.,,:,:ii:,    .;;;i;i;;;i;;;;;;r;;;;i;i    ,ii,,.,.,.,,:,,,,.,,,,:.,,,,..Z7    
      Xa; .,.,.,.,,:,:,::i::     .:;;;;;;;;;;;;;;;;;;;iii;i;i.   .:i::,,.....,,:,::,.:,,.,...r0,    
      ,2a;  ..,.,,,:i:i:i.      :;r;;i;;;;;;;;;;;;;;;;;;;i;i;i.   .,i::,,.......,,,,,,,.,...i2Z     
       rS27. .,,,::i:ii:      .i;;;;;;;;;;;;;;;r;;;;;;;;;;;;ir;.    .i:::,.....,...,,,,,...;;W,     
        XX2S;..,i:i:i.       :;;;i;;;;r;r;r;r;r;rr7rrrrrr;r;;i;i.     :ii,:,,,. ......,..,ri8X      
        82rX2S;,.:::       ,;r;;i;;;;rrr;rrrrrrrrrrr;r;r;;;;;;;;i      .ii::,,.. . . .  i7;ZZ       
       :@02rXSa2r         :ir;;;;;r;r;r;r;rrrrrrrrr;r;r;;;;;;;;;;i    . .ii::::.. .   ,r7i7Z        
       rW08a77X2ZS.      ;;r;;;r;r;r;7rrr7r777r7r7rrrr;r;r;;;;;;;ri  .    :;::::,.  ,r7ri7ZS        
       r@080B2XXXa8ar   i;r;r;rrrrrr7r7r7r77X7X7X7X777X77r7r7rr;;;r:       ,;:,,,:;7Xr;iS08a        
       i@BZ8W@ZSXXSaZZ22Xriii;rrr7r77777777X7X7X7XXX7X7X77rrrr;r;;;r,        :ir7XX7;i7Z00Za        
       @W080B@08SXXSS2aZZZXXr;;rrX7Xr77X7XXX7XXX7X7X7X7777r7rr;r;r;r      .;XXX7r;i7ZW8Z8Za        
        SMB08BWWBWBaXXXSXSSZZZX7SXr;;77XXXXXXXXX7X7X7X7X77rrrr;;i;;;;i ,rS22XX7ri;7ZWW8Z8ZZS        
         @M008WWW0W@W82XXXSSSSaaZaaX77Xi;7X7X777X7X7X7X7X7XXXXSS22aXr7S22SXrr;;r2ZWWB88Z8aBi        
         iMMB08WWWBB@MM@0aXXXSSSS22ZaZZ2SZaa2a20BWBBBB0B0B0088Za2SXSXXXXrr;;728BBWWB888080Z         
         rMMW08WWWBWW@@MMMB0a2XXXXXSS2Sa2a2ZZZaZaZZZaa2a22XXXX7X77rr;;;7XZB@WWBWWB80008BB.         
           iMMWB0BW@WWWWW@MMMMM@B8a2XXXSXXXXSSS2SSSSSSS2XXXX77r7r7rXXZ8W@MM@BBWWBB80000WW:          
           .WMWWBWW@W@WWW@@MMMMMMMMM@WB0ZZa222SSXXXSXXXSSSS2a88BB@MMMMM@BWBWWWB08B0B0@W:           
              MM@@WWW@@@@@W@WM@MMMMMMMMMMMMMMMMMMM@M@MMMMMMMMMMMMMMM@@WWBWW@WW0B0BBBWM0.            
             :MMMMW@W@@M@M@@W@W@@MMMMMMMMMMMMMMMMMMMMMMMMMMMMM@@W@W@W@@@W@BB0BBB0W@M2              
                ZMMMMMWWW@@M@MMM@@W@W@@MMMMMMMMMMMMMMMMMMM@M@M@@@M@M@M@@WWBBBBBWBMMBi               
                 .0MMMM@@@@W@@MMMMMMM@@@@W@@M@MMMMMMMMMMMMM@MMM@M@M@@WBBBBWBWW@MMWX                 
                   .aMMMMM@M@@@@WW@@@MMMMMMMMMMMMMMMMMMM@M@M@M@@WWBWB0BWWWW@@MMWX                   
                     MMMMMMMMMMMWWB088BW0@@@@M@M@M@M@M@@@@@@WWWW0BWWW@W@MMMM8r                     
                       iZMMMMMMMMMMMMM@MWBBWBWB@W@@M@M@M@@@M@@W@@@@MMMMMMMBX.                       
                          i2Z0MMMMMMMMMMMMMMMMMMMMMMMM@M@M@MMMMMMMMMM@Z7.                          
                                ,XZ@MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0ar,                              
                                      ,i7XZ8BWMMMMMMMMMMMWB8aXr:                                    
'''
if a == 'infj' or a == 'INFJ':
      print(infj)

estp ='''ESTP 조각도구
당신은 감각적인 조각도구 같은 사람!
뛰어난 관찰력을 통해 결과에 대해 즉각적이고 현실적인 접근을 하는 편입니다.
이론적인 개념 설명은 지루하게 느껴지고, 활동적으로 움직여야만 속이 시원한 당신은, 편안하게 매 순간을 즐기며 임기응변으로 문제 상황을 잘 모면합니다.
                     .::.       Jvs   vr     DY  rL     L r:. .  :b:  .E.     P.                    
                  .rri:.r.     jg gi   S    sP    v.    X: i     :Y    .E.   v1                     
                  i.    Y      Xu Q:   iJ  rQ     .i   .R  .:   7S      :E  .M.                     
                  .i   :X      Y1 Q.    2. b:      v   KY   :   q.       Ki 1L                      
                   r   Z:      .M B     .S 2       7r rg     irrj        JP7Q                       
                   .i.7X        BBB      B2D       rBgB:     LBB1        JDBg                       
                    sEBi       .RBR      KBQ.      .RBB      iQQq        rqBg                       
                    :BBi       .gBg      5BQ       .dBQ      rRBq        7SBQ                       
                    :BBr       .BQQ      2BB.       dQB.     rQBg        rXBB                       
                    .BQ7       .BBB     .DBB.       EBBi     r2XI        v25Ei                      
                    :gBY       .v7E     .7:v:      .XrSs     7v.v:       v1iJr                      
                    :7J2       .:.7.    .:.7i      .srLU     LLiYr       vj71v                      
                    r7Ju       :i:u.    .ri77      .27s1     vvivr       v171Y                      
                    rvJS       i::vi    .v:77      .U7vI     Yvi7v       Lv7JJ                      
                    7ruI       i::Li    .7:iY      .2vY2     vY:7Y       LY7us                      
                    r7u5       r::vr    .7:rL      .s7s5.    vvir1       JYrYu                      
                    7r1I       r::vr    .r:iu      .JrY2.    7Y:7u       vYrY1                      
                    rrL5       i::7r     r.iY.     .jv7S.    7v:r2       vYrv2                      
                    7rv5       ri:vr     r:iJ.      U7v2:    rs:rU.      7srs1                      
                    rrvS       v::77     7:iJ.      17vXi    is:rI.      7Yr7I                      
                    7iUI       :::7r     r:ij.      U7vXr    :s:r1.      rLi71.                     
                    rr1S       :..rr     r.iJ:      Yrvgi    :s.iu.      rviL5.                     
                    7i12       iY.ri     72:u:      YLv57    .J7iY:      isiBX.                     
                    DvJI       vq.rr     vb:s:      jQ757    .ug:Y:      iviQq.                     
                    QrUU       rj.7i     iS:Yi      sgrUJ    .1Mi7i      iL:EX.                     
                    KvJ2       rI.r7     :Pivr      7b72j     vEi7i      iv:Bd.                     
                    BLJ1       7P.77     :E:vr      7QL11     sBrrr      :L:MI.                     
                    brL2       rr.rr     :vi7v      rDr1U     vd:7r      :7:5K.                     
                    Irv2       rS.7r     :Prv7      rPvsS     vI7rv      :v:PX:                     
                    Er7S       ii.rr     :risY      rD71S     vbir7      :vir2:                     
                    riv2       :i.L7     :7iLY      isvjX     Lrirv      :L:j2:                     
                    7r75       ::.7r     :ii7u      :UrJX     7jirv      :LiiJi                     
                    iiYI       :..ri     .i:7J      irrYP     Y:.iY      :J:rJr                     
                    irvI       :..ir     :i:rI      :LiLX.    7r.rY      :Liiji                     
                    iiY5       :..r7     .i.r1      :Lr7q.    vr.is      :Yiisr                     
                    irvI       :..i7     .i:iU      .LiLP.    r7.iY      :vi:ui                     
                    rrLI       ...ir     .r.i2.     .Lrvd:    r7::J.     .siisr                     
                    :rvI       . .:7     .i:iI.     .srvP:    iv.iY.     .vi:ji                     
                    iiYu       ...i7      r.is.     .LirEi    :7.:L.     .v::vi                     
                    :rvU       ...iv      i::v.      sirP7    .v.:v.     .7i:v:                     
                    ::vu       ...ii      :.:v.      vriSr    .7::s.      v::7:                     
                    .iv1        ..ir      :.:J.      v7rUi     v.:s.      r::v.                     
                    .is1        . r:      ..:L       i7iKi     r:.r       r:.i.                     
                    .rJu        ..J.      .irP       .i:d7     r:iX       7LjQ                      
                    .2BU        udBi      :IBQ       .UXB.     v7BB       rrDB                      
                     XBK        vSBi      .UDB       .uPB:     viQB       i72B                      
                     uBP        vIBi      .rEB.       XIBi     7rRB       :r2B.                     
                     2BE        7DBi       igBi       jIQv     rrBB       .LsB:                     
                    ii:q        I Pr      :j vr      .1:B.     7. r.      .I  7                     
                    2  J.      :i  g      rr  1      sr g      Y   r       s   7                    
                   iL   X      7.  P7     Y:  D      d. g:    :r   ::     .s   .:                   
                  .7    v7     s   .B     Yi  R.     E  bi   .i:    Y.    ir    r                   
                  :     Yu    :D .. R:    Lr .1:    .P  dr   ::   ...r    S     q                   
                 i:  .rri.    .BU:  rS    .5  r.    .Bi.Ir   r. :i:  i   LY....1J                   
                 rBXj7i         ...        .:        1s :    r..:   .    s. ::vY                    

'''
if a == 'estp' or a == 'ESTP':
      print(estp)

entj ='''ENTJ 아이소핑크
당신은 커다란 계획을 만들어주는 아이소핑크 같은 사람!
솔직한 성격 덕분에 결단력이 뛰어나고 남들을 잘 이끌어갑니다. 장기적인 계획을 주로 하며 목표를 설정하는 걸 즐기죠.
자신의 아이디어를 표현하고자 하는 욕구가 강한 당신은, 전략적인 접근을 통해 손쉽고 빠르게 계획을 진행해 좋은 평가를 받지만, 직설적인 화법 때문에 정이 없고 차갑다는 얘기를 듣기도 합니다.
                                                            ....::i.                                
                                                     ....:::::::.:.::.                              
                                              ....:.:::.:...........:::.                            
                                       ....:.:.:......................::.                           
                                ....:::.:...............................::.                         
                          ...:.:.:.......................................:::.                       
                  ....:.:...........................................:...:.:.i:.                     
                  .:.......................................:.:...........:.:.:i:                    
                  .:................................:.....:...:.....:.......::::i.                  
                   :.................................:.......:.:...:.....:...:.::::.                
                   ::...........................:...:...:.:.:.....:.......:.:.:::.:i:               
                   :::...................:.:...:...:...:.:...:...:.:.:.:.:.:.:.:.:.::r.             
                   :::i.........:...:...:.....:...:.:.:.:.:.:.:.:.:.:.:.:::.:.::::::::ii.           
                   .i:ii.......:.:.:.....:.:...:.:.:.:.:.:.:.:.:.:.:.:.:.:.::::::::::::iii          
                   .r:iir:....:...:...:...:.:.:.:.:.:.:::.:.:::.:.:::::::::::::::::::::...:.        
                    iiiiir:..:.:.:.:.:.:.:.:.:.:.:::.:.:.:::.:::::::::::::::::::.......::7uRK       
                 .. .iiiiir:..:.:.:.:.:::::.:::::::::.:::::::::::::::::::.:.......irs2PDRRQB5       
                 ::...iriirr:..:::.:.:.:.:::::::::::::.:::::::::::::.......::7LSPgMBQQggdZdBv       
                 .:....rrirr7:.::.:::::::::::.:::::::::::::::::.......:ruIdMBBBQQggDgEZbdPZBr       
                 .:....:rrirrv::.:::::::::::::::::::::::.......::7sXdQQBBBQQggZDEgEZEZbdbddBi       
                 .::....:rrrr7v::::::::::::::::::.:.......:rjSEMBBBBQQRggggDDdDEZdZdZbEbbPDB:       
                  :::....:rrrrr7i:::::::::::........:7JKEQBBQBQQMRgMDgZgZgZDdDdDdZdDbZPdPdEB.       
                  ::i:....:7rr7r7i:::::.... ..:7uqgQBBBBBQQMRgRgMDgZgEgZgEgZgZDEDEDbEEDbZdgQ        
                  :i:i:....:rrr77vi.....:rsKZBBBBBBBQQMQgMgMDMDgDgZgDgZDZgEgEDEDEgZgDggQQBBg        
                  :iiiri....i77rrr77USDQBBBBBBBQQQQgQMMgMgMDgDgDgZgDgZgZDEgEgDggQQBBBBQd27:         
                  .riiiri....iv7r7iPBBQBQBQBQQRQRQMRgMgggMDgggDgDgDgZDZgDRgQQBQBBg5Li....rX:        
                   .riiiri....i77rivBBBQQRQMQMQMQgRgRMMgMgMDgDgZMgMgRgBBBBBMPsr:...:7jqEMRB:        
                    :riiiri....rv7irBBQQMQMQMRMRMRMRgRggggDMgRgQQBQBBBEI7i:..:ruSDgQgMZDdgB.        
             .:.:.:..:riiirr:...rvr:gBQMQRQRRMRMRgRgMgRgRMQBBBBBgXsr:.::7YqZQQQMRZDEDddPdZB         
             :........:7iri7r:...77iKBQQMQMQMRMQMQgQQBBBBBME17i::irJSZMQQQggZgZgdZEZddbEPgB         
             .:........:rirr7r:.:.7i1BQMQRQMQRQQBBBBQZKs7iii7YXZQQBRQgMDMDgEDEDdZEZbEbbPEgB         
             .:.........i7rrr7r:.:.rYBQQRQQBBBQMq2v7ir7u5dgBQBRRgMgMZgZgZgEDEZEEdZEEbEPdbMM         
              :::........i7r7r7r:...iQBQQDPIj77rLuXdRQQQQRQgMggggZgDgZgZgZgZgEDdEdZbZdEEZRZ         
              ::i:........i7rrr7r:.  7uL7vYU5ZgBQBQQRQRMgMggDgDgZgZgDDEDZgZgZDZZDgEggRQBQBX         
              :::i:........rvr7rvr7L25bZQQBBBQQQQRQMRgRggggDgDgZgZgZgZDZgEDZgDMgQBBQBBRX7.          
              :i:ii:.....:..rvr7riBBBBBBQQQQRQRQMRgRMMgMDgggDgDgZgDgDgDggRQBBBBBBgILi.              
              :iiiir:........7vr7:qBBQBQQQQRQMQMMgRgRgggMggZggggMgMgQBBBBBBRbJr.     .r.            
               iriirr:.:.:.:..7vrisBQQQQMQMQRQgMgRgRgggggggMgQQBBBBBBBZ57:.     .irJSZQs            
                iriirr:...:.:.:77i7BBMQMQMQgRgQgMgRgRgMgQQBBBQBBQKsi.     .:rsXbgRQRMgBi            
                 rrrirr:.:.:::.:77iQBQRQMQMRgRgQMQRQBBQBBBBD1r.     .:rjSZgQQQRQDgdEbDB:            
                  7riir7i.:.:::.:7ibBQQMQRQRQQBBBBBBBMqv:     .:rsKEQQBQQRRDgZZEZdEPbEB.            
                   7rrr77r.:::::.:rqBQRQQBBBBBBBbji.     .iuSgRBQBQQgRggEDZDdEdZdEdbPgQ             
                    v7ri77i.:::::..uBBBBBQg27.     .rLXDQBBBBQQgRggDgZDEDEDdZEDbZddPEDB             
                     v7rr77i.:::::.:bS7:     .iJKgRBQBBBQQgRggggDgZDEDZZZDEZEZdEdEPEbMR             
                      Yr7r77r.:....    .iLKDBBBBBBBRQMRgMDgDgDDZDEDZgEgEDEZdDEZdZEgggQQ             
                      .sr7r7vr...i71XgQBBBBBBQRQMRgRgMggDgDgDgDDZgZDZDZgZDZggRRBBBQBBQL             
                       .J77r7rbBBBBBBBBBQQQRQMQgMgRggggggDgZgDgZgZgZggggQQBBBBBBM2r.                
                        .177ridBBBQBQQRQQQgQMRgRgRggggDgDgDggMDgDMgQBBBBBBBbv:                      
                         .U77ijBBQQRQRQMQgQRRgMgMgMDgDgDgDRgQQBBBQBBBgIi.                           
                          :27r7BBQRQMQMRMQMQgRgMgMgRgRMQBBBBBBQBqv.                                 
                           :1riQBQQRRRQRQMRgRgRMQRBQBBBQBBgui                                       
                            i1iDBQMRMRRQMQMQQBBBBBBBQK7.                                            
                             ivKBQQRQQBBBBBQBQBZj:                                                  
                              :PBBBBBBBBBQS7.                                                       
                               rBBBQPv:                     
'''
if a == 'entj' or a == 'ENTJ':
      print(entj)

entp ='''ENTP 글루건
당신은 거침없는 글루건 같은 사람!
잔머리가 좋으며, 활기찬 에너지를 바탕으로 지루한 일상 바깥의 새로운 도전을 두려워하지 않습니다.
특유의 영리함으로 여러 가능성을 잘 분석하고, 위기 상황을 어떻게든 모면하죠. 하지만 한 번 굳어버린 본드를 돌이키기 어려운 것처럼,
당신은 이미 무계획적으로 저지른 일들에 대해 감당하기 싫은 책임을 지게 되곤 합니다.
                                                              .                                     
                                                           7SDDgS. LP                               
                                                       .JSdEPXKKEdERBZ                              
                                                    .jdMMBDK5XIX5KI5KBg                             
                                                 .1EgdPDBBBMEPXI5252UXBZ                            
                                              :UZMddMBBBgi  iqdXI5252UIB5                           
                                           .YqBQgBBQBDi      .sKX2S252IXQ                           
                                        .sqZPKuXQB1:          iSSI2S255qbs                          
                                     .YqZPq5I251q.         .75ESI252S2SSPQP                         
                                  .sKZPq5S2SI52SIPi  .  .vdQgd5SII25II2KXEBv                        
                               .LKDbPSX5S55252IU5SgSLuXPQgdSSI5I5U52525SPdQs                        
                            .vKEqX5S2K55I5I5252I2IIPPZbbXSI525I52II5U5XPED7                         
                         .YXEPX5qPb5525252I25UI25IS2S55II2II52IIS25ISSqP1                           
                      .LKDPXIqPPqXIS552SIIIII52IU5I52I25252525UI255S2XXL                            
                   .vKZPqIqKdPKU5SPPXU52S252SSS2I25IS2525252S25252S2SIK                             
                .rSZPKIXIPPK2SSPPq2U5K25UII5255IUIUIU525252I25252II5USq                             
              r2ZdqSqPEKI2SSPPq2IIPqqSI25I52I2SSIUIUIU5UI252S252I2I12UPs                            
            rddP5qPEPKISSIXP2IIqqq5S1IIS55UIU5U5ISIS55IX555SI52525UUu2Id2                           
          .SDKPKPPq2ISqPP2IUqPPS5UI2S552I2SIX5S5SSSIX5K5SIX5S5S5SI511jIIEdi                         
         vEdKKPPIISqqq555qS5XX1IIXIXII5S5XXKXKXqSXSKSK5X5X5X5XSX5K5XUUj1IPZU                        
       .ZEq5KIS5PqqIS5KqPKXUSIX5S55IKSKXPPbPdEDZDddPPSX5XSXIXSSSKSXSKSIu1UKdE:                      
       YQP5K5XIKSIIKqPSS2IIX5SIXSKXqKPPddgMQMDdEdgMQRgqPSX5S5XSX5S5XSKX5UU1SKgJ                     
       .QPX5SISUIPPS5U22SIX5XSKKPPdbggRgE1r.       .i5ggZKK5S5X5K5X5X5XSX22uI5ZP:                   
        rQdPXK5SIX2I25IXSKXPKPPZDQMMKs:.             .ivPQZPSXIX5XSX5X5KSXI212IPZY                  
    ...  rQQZPbqqXPqKqqXPPEEgRRdI7.                   .  iPMEXK5X5SSX5X5S5XS51UUKEP.                
   :....   YPEEgRQ2gDggDgMgbsi.                        .   vggKKSXSX5KSX5X5KSX2I15Pg7               
                :r1PqqPX1i                            .     .XQdPSX5XSKSX5S5XXX52u5SDX.             
                  .    .                              .       rggbSK5XIXSX5X5XSKSS1IIPE7            
                 :.    :                              .        .KMEKqSXSXSXSX5XSXSXUIIqZX           
                 i    ..                             .           7DgqqSXXX5KSXSXSXSXI2U5bDi         
                :.    :.                             .            .5QdPSKSXSKSXSKSKXq552SKg1        
               .:     :.                            ..              7ggbXKSKSXSXSKSKSqXX25SEPi      
               i      :.                           ..                .2QDPqXqXqXKXXXXSqSKIIIPd1     
              .:      .                            :                   :MBPPSqXqXKXKSqXqSK5SIKdEi   
              r       .                           .                      uBgbKqXKXqXKXqXqKqS55XPQs  
             i.   ..  :                                                   :MQZqPKKXKXKSqXKKqXX5qQs  
                    ...                                                     uQgPPKqXqXKKqXPXqXqEM   
                                                                             :gQPqKPXqXqKqXqKPEBi   
                                                                               dMqPXKXqKqXPqdRB1    
                                                                                DZXKSKXqKPbQBZ.     
                                                                                7MbqqXPPERBP:       
                                                                                 QBBRRgQBb.         
                                                                                 :vsKbggr    
'''
if a == 'entp' or a == 'ENTP':
      print(entp)

isfp ='''ISFP 물통 
당신은 잔잔한 물통 같은 사람!
사람들 사이에 웬만하면 조용한 편이라 무뚝뚝해 보이기도 하지만, 분명히 다정한 면을 가지고 있습니다.
다양한 상황에서 나름대로 유연함을 발휘해 자신을 지켜내려 하죠. 논쟁이나 갈등을 싫어하는 당신은,
자신만의 테두리에 담겨있는 걸 좋아하지만 물처럼 자연스레 흘러가는 것을 지향하기 때문에 누군가의 속박 역시 매우 싫어합니다.
                                                                                                    
                                      ..,,:,,,::i:i:i::,::,:,..                                     
                                   .iiiiir77XaZ8Z08088ZZa2XX7r;;i;.                                 
                                 .;7;XZ8088ZaSSXX7XXXX22Z80BWBB8ZXS:                                
                              ,;7XXXX2Xr  ii:iiii;;;ir;r;r;rr 77XSZBa2aXi                              
                            irXXXi,  . i;7rrrr;;;r;r;rr777r;;77r;:.   ,iXaZ7,                           
                         .;XXXi.         .,:i;;7r7777777;;::.             .i2ZS:                         
                       .rXSr:                                                ,7ZS:                       
                     .;XSr.                                                    7aS.                     
                    :XS7,                                                      .7Zr                    
                   iXS:                                                         ,a2,                  
                  ;S7                                                             XZ;                 
                 ;S;                                                              ;Zr                
                ;S;                                                                :Z7               
               :S;                   ,:iirr77XXSSSSSXX7rr7;;i:..                    :Zr              
              .X7            .:irXS2aaZZZZZZZZ8Z8Z88880Z88888ZZaaSXri,.              ;Zi             
              rS         :iXSZaZZZaZaa2222S2S2S22a2aaZaZZZZZZZZZZZZZZZa2Xr:.           S2.            
             ,2:     .irXSaaa2a2a22SSXSXSXSS2S2S2S2S2222a2aaa2a2aaaZZZ888ZZaSr:       .Z;            
             77    irXSa2aS;ii;XS22a222222222a2a22S2222a2a2a2aaZZ8808Z2XXSSa2aSX;,     X2            
            .X,  ;XXaaa22SX;XXXr;ir72ZZaa2aaaaZaZaZaaaZaZaZaZZ88BZ27;iii;rrXSS2SX7r,  :Zi           
            :X iSXSa22SSSSXXSZa2Xr::,iXZZZaaaaaZaZaZZZZZZZZ88B82;:,i;7XSS2XSXXXS2277;  ar           
            ;rr7iXa22SSSSSSXS22SSXSXr:,:XZZaaaZaZZZaZZZZ8ZZ80Si,i72aZaa22SSXXXXXSSaS;r:XX           
            iXr,rZ22S222S2XXXSSSXXXSSS;:,7ZZZZZZZZZZZZZ8Z88Z;:iXa8ZZaaS22SXXXSXSXSSZX;7a7           
            7Xi,SZa22S2S2SSXXXSXXXXXSS2ri:XZZZZZ8Z8Z8Z8Z8ZZr:;S80ZZaZ2S22SXXSXSXSX22Z;;2X           
            7Xi:;8aaS2SSXSX77XXXXSXXXS2Sii,:::,::i:::iii:i:ii780ZZZZa2S22SXXXSSSXSSaa;iXX.          
            r7i::78ZaSSXSXXXXXXXXXSXS2Zrii;;;iii;iiiiiiiii;iii8B8ZZZaXSS2XXrXXSS22aZXi;2a           
            rX:r:,;aZaSXXXXS7XXXXSSS2ar::rS277777X7X7X7XXXXr::;8B8ZZ2XX2SS7r7SXS2ZaXi;iZZ           
           iXX,iri,,7S2SS2aX7XSXSSaSXi,,rSaX7r77X777777XXXSXr:,,S0BZaSSSSX7;XS22aX;:;r.BB,          
           .rZ:,i7;i.,i728ZS7S2aSX;i.:iXS2SSr7r77777rXXS7XX2X7i,.:XZa2S2SX77SaS7i::rXr.M0i          
            ,X::i;X7ri:,:i77X77;i,,:rX22aS2X77777777XXXXXXSXSXS7;,.,irS22X7r7i:,:;7XXi:WS           
             .:ii;;r77rri:.,,:::irX2aaaaaa227X7XXX7XXSXXXSS2SSS2SS7r:::i;i::,:irrXXXr;:,            
             ,iiii;;rr77Xrr;;ii:i:ii;;7XSS22XXXXXXXS2S2SSSa22XXXX7r;i:i:::i;rrX7XXXrr;i.            
             ,r;i;;r;;;rr77777rr;;ii::.,.,,::,,:iiiiiiii:i::,:,..::ii;;rr777777X77r7rr;             
               :r;;;r;rrrr7r7r7r7r777rr;;iiii:,:i:i::::::iii;i;i;rrr7r7r7rrrrr7r7r77Xr,             
                ,r;;;r;r;rrrrrrrr7r7r7r7r7r7r7r7rrrrrrrrrrrrrrrrrr;r;rrrr7rrrrrrr77Xr.              
                 :;;r;r;r;rrrr7rrrrrrrr;rrr;rrr;r;r;rrr;rrrrrrr;r;rrrrrrr;rrr;rr777i                
                 :i7rr;;i;;r;rrrrr;r;rrrrr;r;r;r;r;r;r;r;r;r;r;;;r;r;rrrrr;r;r;rrr;:                
                 :iirrXX7;i:;;rrr;r;r;rrrrrrr;r;r;r;r;r;r;r;;;;;r;r;r;r;;iii;r7r7;r,                
                 ::;iirS288ar;;;i;;r;r;r;r;r;r;r;;;r;;;r;r;;;;;;i;;;;;;ii7X2SS77r;r.                
                 ,ii;i;;7SBM8rSXXrr;;i;iii;i;;;;;i;i;;;i;iiiiiiiii;;rrX;0MWaX77rriX                 
                 ,:;i;i;;XaBZi7XS22a2SSSXX77;r;;;;i;i;;;;rr7r77XXXXXXXr;W@8Xr7rr;r7                 
                 .ii;;;;rr288:;;;;r7XXS2aaaaaaaaa2a2a22S2S2SSXX7X77r7rir@02rrr7r;r;                 
                 .:i;;i;;rXZ8iir;;i;i;;;,i;;;rr7r7r7rr;rrr;;rr;r;r;r;r:S@ZXr;rrr;X:                 
                  :i;i;;rrS28ri;r;r;r;7..:,ii ,rr,..:;.:r.  r;;;;;r;r;:Z@2X;rrr;;X,                 
                 .,ii;;;;rXaZ7:r;r;r;;ri    iX.,.. ;S; ... :r;;;;;;r;;:WB2r;;7r;;X                  
                  ::;i;;rrX28Xi;;;;;r;7, :WXrW7  ,  M: S2X7 ri;;;;;;;i;@0Xrirrr;7r                  
                  .ii;i;;rX2Z2:r;r;r;;r: ;M. 0@:.;M;Zi.BZ2; r;;;;;;r;:7MZX;;;rrrXi                  
                   :;i;i;;XSZaiir;;;;;7:  MZi8M iaW 8: XX7, r;;;;;r;;,aMZ7;irrrrX                   
                   .iri;;;72a8i;;;;;;rri   Z707 2M .M:.B82; ;;;;;;;;i:0@27i;r77X:                   
                     ir;;;X2Z07:;;;;;;r;:  MWBi :MS,@,,882r r;;;r;;;iiMB2;ii7X7.                    
                      :77XSZaZXi;;;;;;ri   2ZrS:    r :8SXi r;;;;;;;i7MMa7;rX;                      
                       .i;r,  ;;ri;i;;;;.   .      ..      ,ri;;;;;;r: ;2XX7:                       
                              .7;;;;;;i;rr;;iiiiiiir;;i;;;i;i;i;i;;rr:                              
                               :7rr;;;;i;i;i;;;;;;;i;i;i;;;i;i;;;r77r                               
                                .:irr7r7;r;;i;i;i;i;i;i;;;;;;rr7r;i:                                
                                      ,,iir;rr7rrr7r7r7r7rr;;:,            
'''
if a == 'isfp' or a == 'ISFP':
      print(isfp)

isfj ='''ISFJ 원형템플릿
당신은 원형템플릿 같은 사람!
자신의 자리에서 조용히, 세심하게 제 할 일을 해내는 책임감이 있습니다.
언제나 성실한 태도로 철저함을 보여주며, 다른 사람이 무엇을 하려는지 잘 알아채고 도움이 되어주려 하죠.
어지럽게 삐뚤어진 모양을 못 참는 당신은, 늘 정돈된 환경을 위해 노력하고 있습니다.
                                                                           
                                                                           
                                                                           
  vPBdgBQZQQQMREBRZQRRBQRQBBBBBBBQBBBBBBBBBBBQBBBQBBBQBBBBBBBBBBBBBBBBBBBB 
  PdqUuPU1P5UbS5EKIZP5ZPSdPqZMKEgPDBPgBEgBZMBRZBQgBBMBBRBBgBBQQBQBBRBBQBBB 
  51LLJY1Juu5jS2XjP1b5KZXZdKgPdQZEMEDMgZRgRgQQRgQMMMQgQRMQBgDgBQgdBQgqMQgB 
  U5J2uuLYYJ7viL:J.j.7i.u :Y r7 iL .2  P  7v  P   b   P   E    K.    :IqBB 
  2Uj1X5IJUJ7L7Y7s:s.7r.j.iv rL 7v :I  P  vv  d   d  .D   g    P:    r5PBB 
  U2JJXgRMMPPKMdBgB5gqgBdBgqBgdBQDBQPBBRBBERBBRBBBRBBBRBBBQBBBBBBBBBQBQQgB 
  5Uj2Sii:rIS2XvvrLqSXPLULPgBEP25dQdRDEqQQDQQQMQBQBQBBRQBBBBBQBBBBRQBQBRgB 
  2IUj      Uq     .PJ      uZ:     7Qr     KQ:    iQP   .ZQ.  :Mg.JBX:MgB 
  UIg.      rL      q.      .b       Q      .P      B.     vu   IB     sBB 
  UIIL      JK      Pv      ug.    rB:     2R.    :BX    EQ.  .gD. sBXiggB 
  5UjSIi::iUqXPriivPqq5r77KqPZI1uSgPRKdKZggMZgZgZRQBBQQDQQBMggBQBBBQBBBZgB 
  2UY12PQBKS112KBBdq2I5EBZKbEQgBQPKXXZBBBBMDgQPPPQQBBQQBgMgdbgBBgPPbQBMZEB 
  U1JUKXqXXK5jjSb1IjIP511qdYrrrugPKXgEv::.rKQPP:       igMPPR        iQQgB 
  uS2Sr    :III1     .25Kj       PPZ1        iMdR.           5MMZ      gQB 
  IUq:       Zb        .EP         .QE          1Bi             BB:    .BQ 
  USP:       RP         Rq          QE          jB:             QB.    .BB 
  IU1U.     1IX7      uXbr       jEDr        .DDd            7QMP      KBB 
  2IsIK2uIYP1ujKSv77LPK25ZIi...7PZ5P    .LgZqRZi      .5BbbQZ.       .bBZB 
  S2uJuUbEJv7r7vu5QZ511u1UPPgQDEP5SSPZQZBQQMdqPqgQQPBERBQdPKdMBZ1L1ugBBEgQ 
  Kq1S251uBRdBBBduKPPbIPKqKPbZdEPEPdbDdgMRZgEEEZZMgQBBRMDQgRMQQBBBQBBQQRQB 
  jPXSXXXUBQBBBBBugQBBPQBQQQBBBQRBgEgEgDDZgDggggMgRgggQRQBBMQQQQQRQQQQQRBB 
                                                                           
                                                                           
'''
if a == 'isfj' or a == 'ISFJ':
      print(isfj)

istj ='''ISTJ 가위
당신은 흐트러짐 없는 가위 같은 사람!
매사에 신중하고 철저한 성격으로, 확실한 것을 추구합니다. 자신이 할 일을 계획에 맞춰 꾸준히,
착실히 해나가는 편이라서 대체로 그 결과는 좋습니다.
비뚤어지는 것 없이 체계적으로 정확하게 잘 나아가고 있다고 느낄 때 가장 기뻐하는 당신은, 때로는 사람이 아니라 로봇처럼 보이기도 합니다.
                                                                                                    
                                                                  :X8WM@WZi                         
                                                               :Z@MMMMMMMMM@                        
                                                             ;WMMMM@arr7S0MM2                       
                                                           rMMMMMS       ,MMa                       
                                                         .@MMMB:        XMMMi                       
                                                        2MMMB,        ,@MMMS                        
                                                       @MMM;         ZMMMM2                         
                                                     .MMMB         XMMMM@X                          
                                                    .MMMa        .@MMMM@7                   ,,,     
                                                    MMM2        SMMMMM@;                XBMMMMMMB.  
                                                   ZMM8        WMMMMMW:              ,0MMMMMMMMMMM: 
                                                   MMM,      iMM@@MM8              7MMMMMW:  .;BMMW 
                                                  XMM0      rMM@@@M2             aMMMBMM7       MMM 
                                                  aMMa     XMMMMMM0           ,0MMM0BMZ      . iMM0 
                                                  ZM@@Z7r;0MMMMMMW,         ;WMMM8aMM,        .MMM: 
                                                  0MW@MMMMMMB8XS          7MMMM02WMS         .MMMX  
                                                  MMWW@MMW02r          XMMMMM0a0M8          iMMMS   
                                                 :MMWMM@02i           iMMMM0aWMB           aMMM7    
                                                 0MMMMM07             MM@BBMM8.          iMMMBi     
                                                rMMMMM0;            7MM2@MMS           :WMMMZ       
                                                X0X7SS;            XMMWB0:           rMMMM0:        
                                                 .,,,i,          ;8MM@M8          i8MMMM8i          
                                                ,;;i;i         i0MMMM@@@2:.  ,7ZMMMMMB2,            
                                                ;;i;;:      ,SMMMMMM@MMMMMMMMMMMMMWai               
                                               i;iii:rr;;r222WMMMMMMMMMMMMMMMMB2r.                  
                                              :i:,:i.2Z22a2ZZBMMMMMM@0aX;i,.                        
                                             rSXXXi:,7Z2ZZZS7;M@a;.                                 
                                           ,2aX22ZZ,,a02r,                                          
                                         ;XiXaS8Zra;2X,                                             
                                       ;ZX:i,r7XaX:i                                                
                                     iZ8X:iii::::                                                   
                                   i20Z7ii:iii;i                                                    
                                 iaZZ2;ii,7;i;:                                                     
                               i28aZX:::,7ZXi,                                                      
                             :aZa2a7::ii2a7:                                                        
                           :2Za22Zr:i;722r,                                                         
                         ,2ZZ22aa;:i7aS7;.                                                          
                       ,S8Z222a2i:;r;rXi                                                            
                      S8Z22aZaS:i;r;r7:                                                             
                    X8ZaaZZZXr:i;7r7r,                                                              
                  788aZZ8ar.,:ir7rX;                                                                
                ;88ZZ08S:  :i;rr7X:                                                                 
              iZ0Z80Zr    ;;r777r                                                                   
            .a0000S:     r;rXXXi                                                                    
           XBBBZ7       7;rXXX:                                                                     
         70W0ai       .X;7S2r                                                                       
       :0@07.        ,X;X8Z:                                                                        
     .ZMZ;          ,X;S8S                                                                          
    XWa.           ,X;a8;                                                                           
    i             ,X782                                                                             
                 ,SXZ;                                                                              
                ,SSX                                                                                
               ,2X:                                                                                 
              iZ;                                                                                   
             .S:    
'''
if a == 'istj' or a == 'ISTJ':
      print(istj)

infp ='''INFP 스케치북
당신은 뭐든지 그려내고 싶은, 스케치북 같은 사람!
어떤 문제든 이상적인 해결 방안을 떠올릴 수 있으며, 작은 것에도 호기심이 많습니다.
백지를 서서히 채워나가듯 상대의 마음을 스스로 이해하려 하는 경향이 있죠. 본인만의 작품을 마음속 깊은 곳에서도 자유로이 그려보는데,
그 평화에 위협이 되는 소란스러운 것들을 무척 싫어합니다. 낯가림이 심한 당신은, 그 평화만 계속된다면 생각보다 새로운 환경에 잘 적응하는 편입니다.
                                                                                                    
                             ..:.. .   ..... .                                                      
                            KsssjJXPq7. ...............                                             
                           ig     :7MBL  . .....................                                    
                           iBPQDj7r.    . . ... ... ..................... .                         
                          :D  rIIjSBBv ............... . . .........................                
                          :Mr .  .  7:  . ........... ............... . . . ........... i.          
                          IsJQBBK5qL   ............... ... ..... . . . . ... ... .....  s           
                         ig     .:PB5 ..... ......... ... ....... . . ... ... ... . . ..v           
                         rgQKBS7i.    .. . ......... ... ..... . ............. ..... . :i           
                        :g  .vKJIBB5  . ... ..... ..... ......... . .................  7.           
                        :Du..  .  ii ......... ....... ..... . ... ... . ............. Y            
                        S7XJBBEUqv. . ..... . . ... . ... . . ... ..... . ... . . . . .7            
                       iE     .iPBP  . ... ... ........... ......... . . . . ... ...  :i            
                       iPBIXSr:.    ..... ........... ..... . . . . ....... ... ... . v.            
                      :g   r2I5BQX  ............ ... . . . ............. ... ... . .  v             
                      iKJ.   . .sr  ..... ... . . ..... . ..... . . . . . . .......  .v             
                      1vQqXMK1s:   . . . . ..... ... . . . . . ... ... . ... . ... . i:             
                     rb     i7QBR ..... ... . ... . ... ..... ............... . . .  7.             
                     iIBZi.:.      ... ..... . ..... ........... ..... . . . . . .   s              
                    rb.:riLXPQB7  ....... . ....... ........... . ... ... . . . ... :7              
                    rIi    ..vBI ........... ... ..... ... ... . . ... . . ..... .  i:              
                    vYBQPvj7:     . ... ....... . . . ... ... ....... . ... ... .   L.              
                   jK    .JXBBd  . . . ....... . . . . . ... . . . . ... ..... . .  L               
                   iuU1.  .  :: . ... . ... ... . ..... . . ... . . . ... ..... .  .7               
                  :Ii5BRbPJ2i    ......... ... ....... ....... . ... . ... ... ... r:               
                  u1.    iLQBE  ... . . . ... ......... ... . . ....... . . .....  v.               
                  rjdBdv:.     ....... . . ..... . ..... . . . ... ....... . ...   Y                
                 1S.:vKbqSBQi . . ......... . . . . . ..... ....... . ..... . . . :r                
                 uL:    .:2Bu  . ....... ....... ... ... . ... ... . . . . . ...  r:                
                .7sKBBBv:     . ..... ... ... . . . ....... ... . ... . ... . . . s                 
                b1. .i1IXBBu . ... ..... ... . . . . . ... ..... . ... . ... . . .v                 
                svri.   .:Pi  ... . . ..... . ......... . . . . . . . ... . . .  :r                 
               rr7sBBBJr:    . ............... ... . ... . . . ... ... . .....   7.                 
               dL.   iuSBB1  .... ..... . . ..... . . . . ... . . . . ..... . .  L                  
               Lv7j7:    i.  ....... ... ..... . . . ... . . . ... ... . . ...  .L                  
              5riiEBBJYv.   ..... ..... . . ... . . . . . . . . . . . . . . . . :i                  
             .X7.   .LIBBL . . ... . . . ..... . . ... . ... ... . . . . . . .  7.                  
              vJr25r.       . ..... . ....... ..... . . ..... . . . . . . . .   J                   
            .Dr::sbZU5X7   ... . ..... ..... ..... . ... ... ..... . . ... . . .v                   
            ibJi.  :r2BBi ... ..... . . . . . . ..... . . . ... ... ... . . .  :r                   
             .iJu1i        ... ... . . ... . . ... . . ....... . . ... ... .   v.                   
                ...             . . . . . . . . ......... . ... ... . ... . .  Y                    
                  .27r:.                 . . . . . ..... ... . . ... . . . .  .v                    
                  .XgRBBBBBDPjvi:.                  . ... . ... ... . . . . . i:                    
                         .:vuPDQQBBBgd2Yr:..                   . . ... ... .  v.                    
                                  .:r7UKgRBQQgE517i..                 .   . . s                     
                                            .:iY1PdRMQgDK2Lr::.              .7                     
                                                      .:rv2qDgQRMdPUsri..    :i                     
                                                                .:rL1qEgMRgDKg                      
                                                                          .::.        
'''
if a == 'infp' or a == 'INFP':
      print(infp)

estj ='''ESTJ 3D프린터
당신은 상상을 현실로 만들어주는 3D프린터 같은 사람! 명확한 논리와 자신의 규칙에 따라 빠른 결정을 내리기 때문에 어떤 계획을 이행할 때 큰 영향력을 가집니다. 뭉뚱그려 생각에만 그치지 않고, 항상 구체적이고 현실적인 방안을 고려하죠. 만들고자 하는 것을 뽑아내기 위해 효율적으로 세부사항을 잘 정리하는 당신은, 다른 이들에게 마치 불도저처럼 강렬한 인상을 남기곤 합니다.
                                                                                                    
                          . ....,:::i:iiii;;;;;r7rX7XXXXSS22a2aaZZ888800BBWBWWWWW@@@MMM0.           
                        XMWW@WBWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW.           
                        i0022ZZ28aaaZZZZZaZ2a2Z2a2a2a2a2222S2S2S2SSSSXSXSXSXXrrZWWB0B@@2            
                         XMX.8WrW:                                             XWM008MWX            
                         SM7,8@rW.                                             X@@000MWX            
                         2MX,0@7W:                                             2@M0B0MWX            
                         2MXi0@rW.                           ,0MW.             2M@000MWX            
                         aMX:BW7B.                          XMMMZ              aWM000MWX            
                         aMX:BW7W.                         0MMM,               a@@08BMWr            
                         ZMX:BB7B.                       rMMMB                 Z@M000MWr            
                         ZM7:BB70                       2MMB;                  a@@08BM@;            
                         ZMX:W07W7:7a077i.            X@MMZ                    Z@@800MBi            
                      . .aM7;W07MMMM@ZMM@a;rX77r;:,iaWWSSM.                    Z@W08BMB:            
                   .;SS7B@MX;W8XWMMBXZ2ir;        iMM,  SS                     8@@00W@0B8MMi        
                 ,72X77.8MMXr@8XMMM;.@0;X,    ,7r7BBX:XSMS                     8MW0BW0WBXWMS        
             .  :X7i7aX:ZM@X;MZXMMMX.MM@Z:   .W@WBZ8@0iM2ZZ                    0M@8BBWBW@MM,        
             .,..   rMM@0W@XrWZX@MMXiW@Z2,   .BZZZ88B2r8SZa                    8MWBBBWWW@@0         
             ,,,..  i@WWZZZZZZZ88ZZ008Z00B0WZWW:X@B0WBZ8WW@MWM@WBW0B0000808800ZWWWBWB0BBW@SrS;      
             .:,.., i88WZZ888800BZ00B00BBWMMX;W8MW08WMBZBaMMMMMMMMMMMMMMMMMMMMMWWBWWZ;B2SMZiZM.     
             ,,.    iMMMM@8888ZZ8M@B8MMMMMMM  8B@0aZ0MW0BZB@222a2ZZZaZ2aBMMMMMWWWWWWBWWWWMaXSi      
               .XZZ2WM@WM8X7X7rZB.  .      .  00MMW@M@20@0BW              ra@MM@WWWW@@@@MM0         
                 78WZ222SS7X77r@8          .X 7B0WBMB270MMZS                  r@WBBBBWBW@MM.        
                   ,XS22Sr777;7M0          @M         X .                      BMWBBWBMB7@M7        
                        ;B0SSBB@Z          MM                                  WM@BW@@@@BMW:        
                        :MMX2MZ8Z         :M0                                 .WMWB8@MB.            
                        :MMXSMZ0a         aM7                                  WM@B0WMB.            
                        iMM7SM80a        iMM                                  .WMWW8@MW.            
                        iM@7SMZ02        MM8                                  .WM@W8WMW,            
                        rM@7aMZ02       iMM                                   ,WMWW8WMW.            
                        rMWX2MZBS       8Mi                                   .@M@B0WMB,            
                        7M@XaM8BX      :MS                                    :@MWW8@MB.            
                        XMWXaM8WX      MM                                     ,MM@B0@MB.            
                        XMWXZM8BX     BM2                                     :@M@W8@MB.            
                        SMWSZM8W7    SMM                                      :MM@W0@MB.            
                        aMWSZM8B7    MM8                                      iMM@W8MMB             
                        2MB28M8Wr   2MMi                                      iMM@W0@MB             
                        ZMB28M0Wr   MMB                                       ;MMW@8MMB             
                        ZMB28M0@;  iMM:                                       iMM@W0@M0             
                        8MBS0M0W;  7M0                                        ;MM@@0MMB             
                        0M0a0M8M:  ZM;                                        ;MM@W0@M0             
                        BMB2BM0M:  @M  20WWWi                                 ;MMWW0MMB             
                        WMBZWMBMr.;0Za8B0888ZZaaZa2a22X2XX7X77;7;;:i::,,., .  XMM@WBMM0             
                        B@00BWWW@@WZ8008aSXXSSSS2S2S22222aZ2Z2ZaaaZZ8Z8Z880BBaB@MW@0MM0             
                       .SXrrr7ri;:r82XXX7a2aS222S2S2XSXXXSSXXSXSSaaa2aZZZZa7. XMM@WBMM0             
                        MM08MM8ir aMX.;X0MMMMMM@WBBZ080BBZZZaaa2a7XZ8ZZZ8WMr  XMM@@0MM0             
                        MM08MMBa0WWMMMMMBaBM2Z87BMMMMMMMMMMMMMMM@:SBr:   .i   XMMM@BMM8             
                        MMBZMM08W88M.    78X7ZW0MMM@@@MWMMM@MMMWM08S:         SMMM@0MM0             
                        MM08M@0MMB0Mr;ZrZM@@MMM@080W@MMMMMBB8BBWMWr           XMMM@BMM0             
                        MM08MWBMMMB0B0MMW0B0Za00WW@WW08a808Z80BWMMS  .        2MMMMBMM0             
                       ;MM00MW0MM@BW@MWW@@@WBWWWB0Z8Z0008888BWB@@M02XXXX7aXSX:BMMM@BMM0::i:::       
                .:;7XXS2B@WBWWWWBZ0BWBWBWW@0WBBBBBWWWBBBBB@@@WB8Za2XX7X7XXS77iBMMMMWMMWr7rS@@,      
           .,;rXXX7Xr7XSZBBWWWWW080WBWBWWWWBWBaW@WWWW@@MMM@MW@WB08Za2222SSXX7r0MMMMMMWXr;;0M@;      
      .SaaZaZa2SSXXXXXXSZZ00WBBBB8BWWWWWWWWWMBZW@W@@M@@@@@M@@@@WB00ZZaa2a22XXX0MMMBZr.;;r7@BMS      
      :M@WBWBBBBBBBBBB0088Z888Z0000WBWWWW@WW@MMMW@W@@M@MW@@@@@W@W@WWWB00ZZaaSa8B27;r7X27rSMMMr      
      ,WB80808080800BBB800B0B0BBB0B0BBWW@W@W@WW@BBW@M@MM@WWW@WWWWWMMWBWMMM@MMMW;;72S2aZ7S28X        
      ,@B088888880808000800000000B0BBB0BBWBWBWWWBWWMMMM@BWBWBWBB0WM@0WWMM@8WMMS7208aaZ8ar.          
      iMM@@BB80800BBB0B0B0B0B0B0BBBBBBBBWBWWWWWWWWM@MMM@@W@WWWWBWWMWBWWBMMaBM82ZB0ZZ02i.            
      .2aZZZWW0WW@WMMMMMMMMMMMMMMMMMMMMM@M@M@M@MW@@@W@W@W@WWWWW@@MMM00B@@M@M@aZZZ8ar.               
            XMMMMi  ..,,ii;rXXSSaaZ800W@MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWW@@@MZ2ZZS:                  
                                        .     .::i;r7XSaa80BB@@MMMMMMM@@W@MMZSr.                    
                                                                    iXMMMMMa:                       
                                                                      r2S2,                         
                                                                                                    
'''
if a == 'estj' or a == 'ESTJ':
      print(estj)
    
enfp ='''ENFP 물감
당신은 알록달록 무한한 가능성, 물감 같은 사람!
상상력이 풍부하고 열정적인 성격이라 새로운 것을 시도하는 데에 거리낌이 없습니다.
그런 자신감을 내뿜으면서도 칭찬은 받고 또 받고 싶은 마음이죠. 물론 칭찬해주는 이에게 그만큼의 감사를 표현해주는 것은 기본, 즉흥적으로 또 다른 일을 시작해보려 합니다.
이런 색도, 저런 색도 섞어보며 그때그때 융통성을 발휘해 새로운 문제를 해결하려는 당신은, 이미 다 엎질러놓고 수습하려는 경향이 강한 탓에 종종 난처해지기도 합니다.
                                                                         ,                          
                                                                        ;7r:                        
                                                                       ir7r7;i                      
                                                                       i :r77r7i.                   
                                                                      .r   :;7r77;.                 
                                                                      ;i:,,...irrr7;,               
                                                                     ;;i::::,,.,:r;rr;,             
                                                                   .;;iii::::::,.,i;;;7;:           
                                                                  ,rii:iii:i,i::,,.:i;;rrr:         
                                                                 ,;iiiiii:i::::,:::,,,ii;;r;i.      
                                                                :r;i:i:i,i:i,:::::,,.. .,i;rr7i,    
                                                               iri;;ri:iXi,,:,:,:,,.. . . ,irrrrri. 
                                                              i;irii:;iX;Xa7,::,.....,...   .:ir7r  
                                                            .i;ii:iir:::i;X2rr:,:,:,:,:::,,,:,ir,   
                                                           .i;iiii:;2S;i:i:,X8a;:::i:i:i:;;rrXi     
                                                          ,;i:i:iii::72X;:::iir:8S:,::iirrrr;.      
                                                         ,;;:i,::iii:::;XZri.,77rXSXii;rrrr:        
                                                        ,:;:i.rSi:iiiii::;2SXi70aiiS0S;r7i          
                                                       rW2;:,7S::i:iiiii::,iX2riS0ZrS2r;            
                                                      ii7;.:77.X;.7;:ii:iii:,:XaX;027i.             
                                                    .;i:,:iS:iSr.XS::i:i:iiii;:;aSrr.               
                                                   ,;i::77X.ra77S7::iiiiiiii;;;irX:                 
                                                  :i,.i7r;,XX;X2i,iiiiiii;;;i;rX;                   
                                                 77 :r:,,i77XSX,::iiiiii;;;;rX7.                    
                                               .7r iZMMM7,:X2;,iiiiii;i;;;i7Xi                      
                                              ,r: XM;@MMMXSX:,iiiiii;;;;;rSr                        
                                             ,Xi,@8MM:;2X27,:iiiiii;;rirXX,                         
                                            ;XiXaXWX0MM0X:,:iiii;;r;;iXS;                           
                                           XXira@270;0Br.,:iiii;;r;;;SX.                            
                                         ,S7:2@@82iBMX: ,iii;i;;r;;72i                              
                                        .i;7WMW0ZMMZri;i:2Z7i;;;ir2X                                
                                       rS: :;20MWX0iir;X8aX:;;;;Sa;                                 
                                     ;82rXX:  a08X;XirZaS;:;;;raS                                   
                                    X80BBS7XXi  ;:SXr28i;:i;;S8i                                    
                                  ;800808W0ZXXXr..,;SX7ii;Xa02                                      
                                  XWMB080Z0BWZXX2Xi.;;i;r2BB;                                       
                                   ,X8WB88808BB8XXSS;:i;aWZ                                         
                                    ..X8WB080888B82X2SXX8r                                          
                                   S0S, .8BB88Z8Z0BBaZMW                                            
                                 .2W@ZXi;rXa0B080800MMa                                             
                                r802;aW@S;;rraB@BBBMM;                                              
.                               78Xi7ZBSr;;Sa;7ZWMM0                                                
                                rWXXZZXXXSZ8.    :.                                                 
           .,,i;XX2aZZ888Zaaa22Z8Z08X7Sa0Wa                                                         
  :SZ80B0B0BBBBB08BB0088Z8ZZ8B08ZaZBBSX7a7                                                          
  rMMWWB0Z8Z8Z8ZZa8Z888Z8Z2XSZ8Z8Z0Wa                                                               
    7Z0BWWBB0080Za0000B8aWWWBB0BW@WX                                                                
        iSZ8BBBBB8BB0Z80888a800aX:                                                                  
               . .                                   
'''
if a == 'enfp' or a == 'ENFP':
      print(enfp)
                                                           
                                                                                                    
                                                                                                    
                                                                                                    
                                                                      

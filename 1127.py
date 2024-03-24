'''
   用伪python代码描述《民法》第 1127 条
   email: majiazhi@qq.com
   2024.03.24 如有不妥，请及时指正

   根据《中华人民共和国民法典》第一千一百二十七条规定：
   “遗产按照下列顺序继承：（一）第一顺序：配偶、子女、父母；（二）第二顺序：兄弟姐妹、祖父母、外祖父母。
   继承开始后，由第一顺序继承人继承，第二顺序继承人不继承；没有第一顺序继承人继承的，由第二顺序继承人继承。
   本编所称子女，包括婚生子女、非婚生子女、养子女和有扶养关系的继子女。本编所称父母，包括生父母、养父母和有扶养关系的继父母。
   本编所称兄弟姐妹，包括同父母的兄弟姐妹、同父异母或者同母异父的兄弟姐妹、养兄弟姐妹、有扶养关系的继兄弟姐妹。”

   声明：本代码只用于说明编程语言的应用逻辑，并不是法律条文在实际应用中的解析，
   由于法律条文内容描述的颗粒度较大，本代码为了在纯代码层面（而非法律层面）
   逻辑的连贯、合理、闭包、一致性要求，在细节方面，并为按法律条文描述，
   请不不要作为法律条文实际参考，需要了解法律条文的实际解释，请咨询法律专业机构或人员。
'''

# 配偶
def 配偶():
     找到的有效配偶 = []
     for 第x位配偶 in 全部配偶:
          if 第x位配偶 当 被继承人死亡时 已离世:
               continue
          if 第x位配偶 结婚证书 已无效:
               if 第x位配偶 重婚 and 不是最早结婚配偶:
                    continue
               if 第x位配偶 离婚后 已不在一起生活:
                    continue
          if 被继承人 有遗嘱表明 第x位子女 无继承权:
               continue
          找到的有效配偶.append(第x位配偶)
     return 找到的有效配偶
               
# 子女
def 子女():
     找到的有效子女 = []
     for 第x位子女 in [婚生子女、非婚生子女、养子女、有扶养关系的继子女]:
          if 第x位子女 当 被继承人死亡时 已离世:
               continue
          if 第x位子女 是 继子女:
               if 第x位子女 无有扶养关系:
                    continue
          if 被继承人 有遗嘱表明 第x位子女 无继承权:
               continue
          找到的有效子女.append(第x位子女)
     return 找到的有效子女

# 父母
def 父母():
     找到的有效父母 = []
     for 第x位父母 in [生父母、养父母、继父母]:
          if 第x位父母 当 被继承人死亡时 已离世:
               continue
          if 第x位父母 是 继父母:
               if 第x位父母 无有扶养关系:
                    continue
          if 被继承人 有遗嘱表明 第x位父母 无继承权:
               continue
          找到的有效父母.append(第x位父母)
     return 找到的有效父母


# 配偶、子女、父母；
def 第一顺序继承人():
     继承人 = []
     继承人.append(配偶())
     继承人.append(子女())
     继承人.append(父母())
     return 继承人

# 兄弟姐妹、祖父母、外祖父母。
def 第二顺序继承人( 被继承人 ):
     继承人 = []
     继承人.append[同父母的兄弟姐妹、同父异母的兄弟姐妹、同母异父的兄弟姐妹、养兄弟姐妹、有扶养关系的继兄弟姐妹]:
     继承人.append(祖父母)
     继承人.append(外祖父母)
     return 继承人

def 按比例执行继承 ( 被继承人 , [祖继承人] , 遗产总金额 , 可继承总数 ):

     for 第x位袓继承人 in [祖继承人]:
          重继承额 = 遗产总金额 * 第x位袓继承人的所得在执行继承时 (含负债) 的占比
          if 重继承额 > 实际从第x位袓继承人所继承金额:
               重继承额 = 实际从第x位袓继承人所继承金额
          if 重继承额 > 0:
               执行第1127条 ( 第x位袓继承人 , 重继承额 )
          

def 执行第1127条 ( 被继承人 , 遗产总金额 ):

     可继承总数 = 遗产总金额 - 债务总额
     if 可继承总数 <= 0:
          return

     if 被继承人曾从他人(祖继承人)处继承额 > 0:
          可继承总金额 = 按比例执行继承 ( 被继承人 , [祖继承人] , 遗产总金额 , 可继承总数 )

     继承人 = 第一顺序继承人 ( 被继承人 )

     if len(继承人) > 0:
          for 第x位继承人 in 继承人:
               第x位继承人继承金额 = 按比例执行继承 ( 第x位继承人 , 可继承总金额 )
               if 第x位继承人 已离世:
                    执行第1127条 ( 第x位继承人, 第x位继承人可继承总金额 + 第x位继承人继承金额 )
          return
          
     继承人 = 第二顺序继承人(被继承人)

     if len(继承人) > 0:
          for 第x位继承人 in 继承人:
               执行第1127条(被继承人)
          return
     
     默认处理 ( 被继承人 , 可继承总金额 ):

     return

if __name__ == '__main__':
     执行第1127条 ( 被继承人 , 遗产总金额 )
          

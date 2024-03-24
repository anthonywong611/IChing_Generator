import unittest

from GUA import GUA 

class testGuaXiang(unittest.TestCase):
   """
   """
   def test_qian_gua_ci(self):
      qian = GUA("乾")
      self.assertEqual(qian.guaCi, "元，亨，利，贞。")

   def test_qian_yao_ci(self):
      qian = GUA("乾")
      self.assertEqual(qian.yaoCi, {
         1: "初九：潜龙勿用。",
         2: "九二：见龙在田，利见大人。",
         3: "九三：君子终日乾乾，夕惕若厉，无咎。",
         4: "九四：或跃在渊，无咎。",
         5: "九五：飞龙在天，利见大人。",
         6: "上九：亢龙有悔。"
      })

   def test_qian_cuo_gua(self):
      qian = GUA("乾")
      qian_cuo = qian.cuo()
      self.assertEqual(qian_cuo.name, "坤")

   def test_zhong_fu_cuo_gua(self):
      qian = GUA("中孚")
      qian_cuo = qian.cuo()
      self.assertEqual(qian_cuo.name, "小过")

   def test_yi_zong_gua(self):
      yi = GUA("益")
      yi_zong = yi.zong()
      self.assertEqual(yi_zong.guaCi, '有孚，元吉，无咎，可贞。利有攸往。曷之用？二簋可用享。')

   def test_feng_hu_gua(self):
      feng = GUA("丰")
      feng_hu = feng.hu()
      self.assertEqual(feng_hu.yaoCi[4], '九四：栋隆，吉。它吝。')

   def test_cuo_zong_fu_za(self):
      ge = GUA("革")
      ge_czfz = ge.cuoZongFuZa()

      self.assertEqual(ge_czfz[5].name, "复")
      self.assertEqual(ge_czfz[2].guaCi, '元吉，亨。')

if __name__ == "__main__":
   unittest.main()
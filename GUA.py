from io import StringIO
from typing import List

import pandas as pd
import json

guaci = json.load(open('./data/gua_ci.json'))
yaoci = json.load(open('./data/yao_ci.json'))
sixty_four = json.load(open("./data/sixty_four.json"))

cuo = {"地": "天","山": "泽","水": "火","风": "雷","雷": "风","火": "水","泽": "山","天": "地"}
zong = {"地": "地","山": "雷","水": "水","风": "泽","雷": "山","火": "火","泽": "风","天": "天"}
bagua_binary = {"地": "000","山": "100","水": "010","风": "110","雷": "001","火": "101","泽": "011","天": "111"}

fangTu = pd.read_json(StringIO(json.dumps(sixty_four)))
names = pd.melt(
   fangTu, ignore_index=False, var_name="外卦", value_name="挂名"
).reset_index(names="内卦")

names['重卦'] = names["外卦"] + names["内卦"]
chong_gua = {
   row['挂名']: {'外卦': row['外卦'], '内卦': row['内卦']} for _, row in names.iterrows()
}


class GUA:
   """
   """
   name: str
   guaci: str
   yaoci: dict[str, str]

   def __init__(self, name: str) -> None:
      self.name = name
      self.guaCi = guaci[name]
      self.yaoCi = yaoci[name]

   def cuo(self, cuo: dict[str, str] = cuo):
      wai_cuo = cuo[chong_gua[self.name]['外卦']]
      nei_cuo = cuo[chong_gua[self.name]['内卦']]
      return GUA(sixty_four[wai_cuo][nei_cuo])

   def zong(self, zong: dict[str, str] = zong):
      wai_zong = zong[chong_gua[self.name]['内卦']]
      nei_zong = zong[chong_gua[self.name]['外卦']]
      return GUA(sixty_four[wai_zong][nei_zong])

   def hu(self, bagua: dict[str, str] = bagua_binary):
      bagua_inverted = {v: k for k, v in bagua.items()}
      wai_gua, nei_gua = chong_gua[self.name]['外卦'], chong_gua[self.name]['内卦']
      chong_binary = f"{bagua[wai_gua]}{bagua[nei_gua]}"
      outer_exch, inner_exch = chong_binary[1:4], chong_binary[2:5]
      wai_hu, nei_hu = bagua_inverted[outer_exch], bagua_inverted[inner_exch]
      return GUA(sixty_four[wai_hu][nei_hu])

   def cuoZongFuZa(self, display_name: bool = False):
      four_sides = [self, self.cuo(), self.zong(), self.cuo().zong()]
      four_change_sides = list(map(lambda gua: gua.hu(), four_sides))
      eight_sides = four_sides + four_change_sides
      if display_name:
         return list(map(lambda gua: gua.name, eight_sides))
      return eight_sides

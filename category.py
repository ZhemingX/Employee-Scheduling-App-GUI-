# list of all departments
depart = ["眼科","肿瘤内二科","胃肠外科","肿瘤外科","肝胆胰外科","内分泌代谢科","肿瘤内一科","泌尿外科","微创外科","针灸科",
          "烧伤整形外科","骨一科","消化内科","耳鼻咽喉科","神经外科","心胸外科","妇产科","神经内科","呼吸内科","骨二科",  
          "血液内科","中西医肾病科","心血管内科","肿瘤放疗科","肛肠外科","中医科","内镜中心","血液净化中心",
          "儿科","康复医学科","整形美容科","放射科","全科医学科","伤科","超声科","康复科","检验科"]

# 37 elements

import random

def get_depart():
    for i in range(2):
        # to get a random order each time, a flexible way for get random order results of schedule
        random.shuffle(depart)
    return depart

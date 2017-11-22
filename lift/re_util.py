# -*- coding: utf-8 -*-

import re

# 匹配电梯详情 设备品种：
# r_device_category = re.compile(u"<p>设备品种：(.*?)</p>", re.DOTALL)
r_device_category = re.compile(u"<p>设备品种：(.*?)\(.*\)</p>", re.DOTALL)
r_rated_load = re.compile(u"<p>额定载重：(.*?)</p>", re.DOTALL)
r_layer_number = re.compile(u"<p>层数：(.*?)</p>", re.DOTALL)
r_rated_speed = re.compile(u"<p>额定速度：(.*?)</p>", re.DOTALL)
r_maintenance_name = re.compile(u"<p>维保单位名称：(.*?)</p>", re.DOTALL)
r_maintenance_phone = re.compile(u"<p>维保单位电话：(.*?)</p>", re.DOTALL)
r_put_into_use_date = re.compile(u"<p>投入使用日期：(.*?)</p>", re.DOTALL)
r_manufacture_unit = re.compile(u"<p>制造单位：(.*?)</p>", re.DOTALL)
r_installation_unit = re.compile(u"<p>安装单位：(.*?)</p>", re.DOTALL)
r_using_unit = re.compile(u"<p>使用单位：(.*?)</p>", re.DOTALL)
r_examination_date = re.compile(u"<p>检验日期：(.*?)</p>", re.DOTALL)
r_examination_result = re.compile(u"<p>检验结论：(.*?)</p>", re.DOTALL)
r_examination_report = re.compile(u"<p>检验报告：(.*?)</p>", re.DOTALL)
r_effective_expiration_date = re.compile(u"<p>有效截止日期：(.*?)</p>", re.DOTALL)
r_buffer_form = re.compile(u"<p>缓冲器形式：(.*?)</p>", re.DOTALL)
r_door_opening_mode = re.compile(u"<p>开门方式：(.*?)</p>", re.DOTALL)
r_heavy_blocks_number = re.compile(u"<p>对重块数量：(.*?)</p>", re.DOTALL)
r_top_height = re.compile(u"<p>顶层高度(米)：(.*?)</p>", re.DOTALL)
r_pit_depth = re.compile(u"<p>底坑深度(米)：(.*?)</p>", re.DOTALL)
r_motor_category = re.compile(u"<p>电动机类型：(.*?)</p>", re.DOTALL)
r_motor_type = re.compile(u"<p>电动机型号：(.*?)</p>", re.DOTALL)
r_motor_power = re.compile(u"<p>电动机功率：(.*?)</p>", re.DOTALL)
r_rated_current = re.compile(u"<p>额定电流：(.*?)</p>", re.DOTALL)

r_list = (r_device_category,
          r_rated_load,
          r_layer_number,
          r_rated_speed,
          r_maintenance_name,
          r_maintenance_phone,
          r_put_into_use_date,
          r_manufacture_unit,
          r_installation_unit,
          r_using_unit,
          r_examination_date,
          r_examination_result,
          r_examination_report,
          r_effective_expiration_date,
          r_buffer_form,
          r_door_opening_mode,
          r_heavy_blocks_number,
          r_top_height,
          r_pit_depth,
          r_motor_category,
          r_motor_type,
          r_motor_power,
          r_rated_current)


# 提前电梯详情
def extract_details(html, url):
    details = ''
    if html:
        fields = []
        if url.split("=")[-1]:
            fields.append(url.split("=")[-1])
        for regex in r_list:
            m = regex.search(html)
            if not m:
                field = ''
            else:
                field = m.group(m.lastindex).replace('&nbsp;', '').strip()
            fields.append(field)

        details = ''.join(map(lambda x: '"' + x + '";', fields)) + '\n'
    return details

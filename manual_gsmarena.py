import json
import os
import random
import requests
import sys
import time
from bs4 import BeautifulSoup

"""
SCHEMA
---

Table smartphone
# id (automatic?)
# name
# brand
# dxomarkScore
# photo (from 'selfie''photo' OR 'mobile''photo')
# bokeh
# preview
# zoom
# video (from 'selfie''photo' OR 'mobile''photo')
# price
# segmentPrice
# storage
# displaySize
# displayRes
# cameraPixel
# videoPixel
# ram --> ambil paling gede
# battery
# imageLink (UPDATE name to image instead)
# launchDate (buat cek 3 tahun terakhir)

table Antutu
id
name
processor (score overall)
CPU
GPU
MEX
UX


Refined, matched with scraping results:
devicespecifications.com Table
id
name
brand
dxomarkScore (from dxomark)
photo (from dxomark)
bokeh (from dxomark)
preview (from dxomark)
zoom (from dxomark)
video (from dxomark)
price (from dxomark)
segmentPrice (from dxomark)
storage (from dxomark)
displaySize (from dxomark)
displayRes (from dxomark)
cameraPixel (from dxomark)
videoPixel (from dxomark)
ram (from dxomark)
battery (from dxomark)
imageLink (from dxomark)
launchDate (from dxomark)

"""

"""
Checking:
# means correct
# DOESN'T EXIST means doesn't exist, need to fill the data manually
"""
gsmarena_smartphone_urls = [
    "https://www.gsmarena.com/google_pixel_3-9256.php", #
    "https://www.gsmarena.com/xiaomi_mi_mix_3-9378.php", #
    "https://www.gsmarena.com/apple_iphone_xs_max-9319.php", #
    "https://www.gsmarena.com/huawei_p20_pro-9106.php", #
    "https://www.gsmarena.com/intex_aqua_selfie-8754.php", # DOESN'T EXIST 
    "https://www.gsmarena.com/apple_iphone_x-8858.php", #
    "https://www.gsmarena.com/google_pixel_2-8720.php", #
    "https://www.gsmarena.com/oneplus_7_pro-9689.php", #
    "https://www.gsmarena.com/lg_g8_thinq-9540.php", #
    "https://www.gsmarena.com/huawei_p30_pro-9635.php", #
    "https://www.gsmarena.com/huawei_mate_20_pro-9343.php", #
    "https://www.gsmarena.com/meitu_t9-9261.php", # DOESN'T EXIST
    "https://www.gsmarena.com/meitu_v6-8921.php", # DOESN'T EXIST
    "https://www.gsmarena.com/samsung_galaxy_s8-8161.php", #
    "https://www.gsmarena.com/sony_xperia_1-9543.php", #
    "https://www.gsmarena.com/lenovo_z6_pro-9642.php", #
    "https://www.gsmarena.com/honor_20_pro-9707.php", #
    "https://www.gsmarena.com/samsung_galaxy_s10+-9535.php", #
    "https://www.gsmarena.com/asus_zenfone_6_zs630kl-9698.php", #
    "https://www.gsmarena.com/huawei_mate_30_pro-9884.php", #
    "https://www.gsmarena.com/apple_iphone_11_pro_max-9846.php", #
    "https://www.gsmarena.com/huawei_mate_20_x-9367.php", #
    "https://www.gsmarena.com/xiaomi_mi_cc9_pro_premium_edition-9943.php", #
    "https://www.gsmarena.com/asus_rog_phone_ii_zs660kl-9770.php", #
    "https://www.gsmarena.com/huawei_nova_6-9971.php", #
    "https://www.gsmarena.com/nokia_7-8907.php", #
    "https://www.gsmarena.com/google_pixel_4-9896.php", #
    "https://www.gsmarena.com/huawei_mate_30_pro_5g-9885.php", #
    "https://www.gsmarena.com/xiaomi_black_shark_2_pro-9779.php", #
    "https://www.gsmarena.com/xiaomi_mi_10_pro_5g-10055.php", #
    "https://www.gsmarena.com/realme_x2_pro-9904.php", #
    "https://www.gsmarena.com/oppo_find_x2_pro-9529.php", #
    "https://www.gsmarena.com/nubia_red_magic_3s-9871.php",
    "https://www.gsmarena.com/honor_v30_pro-9962.php",
    "https://www.gsmarena.com/sony_xperia_5-9814.php",
    "https://www.gsmarena.com/apple_iphone_11-9848.php",
    "https://www.gsmarena.com/huawei_p40_pro-10152.php",
    "https://www.gsmarena.com/samsung_galaxy_a71-9963.php",
    "https://www.gsmarena.com/samsung_galaxy_z_flip-10098.php",
    "https://www.gsmarena.com/samsung_galaxy_s20+-10081.php",
    "https://www.gsmarena.com/oneplus_8_pro-10041.php",
    "https://www.gsmarena.com/motorola_edge+-10153.php",
    "https://www.gsmarena.com/asus_rog_phone_3-10212.php",
    "https://www.gsmarena.com/lg_v60_thinq_5g-10114.php",
    "https://www.gsmarena.com/oneplus_8-10040.php",
    "https://www.gsmarena.com/apple_iphone_se_(2020)-10170.php",
    "https://www.gsmarena.com/black_shark_3_pro-10154.php",
    "https://www.gsmarena.com/sony_xperia_1_ii-10096.php",
    "https://www.gsmarena.com/xiaomi_mi_10_ultra-10358.php",
    "https://www.gsmarena.com/nubia_red_magic_5s-10359.php",
    "https://www.gsmarena.com/vivo_x50_pro+-10212.php",
    "https://www.gsmarena.com/asus_zenfone_7_pro-10360.php",
    "https://www.gsmarena.com/huawei_p40-10153.php",
    "https://www.gsmarena.com/huawei_mate_40_pro-10412.php",
    "https://www.gsmarena.com/google_pixel_5-10385.php",
    "https://www.gsmarena.com/apple_iphone_12-10509.php",
    "https://www.gsmarena.com/lenovo_legion_phone_pro-10361.php",
    "https://www.gsmarena.com/poco_x3_nfc-10415.php",
    "https://www.gsmarena.com/apple_iphone_12_pro-10510.php",
    "https://www.gsmarena.com/google_pixel_4a-10385.php",
    "https://www.gsmarena.com/apple_iphone_12_pro_max-10511.php",
    "https://www.gsmarena.com/samsung_galaxy_note20_ultra_5g_(exynos)-10360.php",
    "https://www.gsmarena.com/samsung_galaxy_s10+_(exynos)-9535.php",
    "https://www.gsmarena.com/samsung_galaxy_s10_5g_(exynos)-9536.php",
    "https://www.gsmarena.com/samsung_galaxy_note_10+_(exynos)-9788.php",
    "https://www.gsmarena.com/samsung_galaxy_note_10+_5g_(exynos)-9789.php",
    "https://www.gsmarena.com/samsung_galaxy_s20_ultra_5g_(exynos)-10081.php",
    "https://www.gsmarena.com/samsung_galaxy_note20_ultra_5g_(snapdragon)-10360.php",
    "https://www.gsmarena.com/huawei_mate_40_pro+-10413.php",
    "https://www.gsmarena.com/xiaomi_mi_10t_pro_5g-10414.php",
    "https://www.gsmarena.com/oppo_reno4_pro_5g-10362.php",
    "https://www.gsmarena.com/oneplus_8t-10363.php",
    "https://www.gsmarena.com/vivo_x51_5g-10364.php",
    "https://www.gsmarena.com/samsung_galaxy_note20_(exynos)-10360.php",
    "https://www.gsmarena.com/apple_iphone_12_mini-10512.php",
    "https://www.gsmarena.com/asus_rog_phone_5-10365.php",
    "https://www.gsmarena.com/samsung_galaxy_s21_ultra_5g_(exynos)-10513.php",
    "https://www.gsmarena.com/zte_axon_20_5g-10366.php",
    "https://www.gsmarena.com/xiaomi_mi_10_s-10367.php",
    "https://www.gsmarena.com/motorola_razr-10368.php",
    "https://www.gsmarena.com/samsung_galaxy_z_fold2_5g-10369.php",
    "https://www.gsmarena.com/black_shark_4_pro-10370.php",
    "https://www.gsmarena.com/xiaomi_mi_11-10371.php",
    "https://www.gsmarena.com/oppo_reno5_pro+_5g-10372.php",
    "https://www.gsmarena.com/xiaomi_mi_11_ultra-10373.php",
    "https://www.gsmarena.com/samsung_galaxy_s21_ultra_5g_(snapdragon)-10514.php",
    "https://www.gsmarena.com/samsung_galaxy_s21_5g_(exynos)-10515.php",
    "https://www.gsmarena.com/samsung_galaxy_s21+_5g_(exynos)-10516.php",
    "https://www.gsmarena.com/samsung_galaxy_s21_5g_(snapdragon)-10517.php",
    "https://www.gsmarena.com/vivo_x60_pro+-10374.php",
    "https://www.gsmarena.com/huawei_p40_lite-10375.php",
    "https://www.gsmarena.com/motorola_moto_g9_power-10376.php",
    "https://www.gsmarena.com/oppo_find_x3_lite-10377.php",
    "https://www.gsmarena.com/oppo_find_x3_neo-10378.php",
    "https://www.gsmarena.com/oppo_find_x3_pro-10379.php",
    "https://www.gsmarena.com/realme_c11-10380.php",
    "https://www.gsmarena.com/samsung_galaxy_m51-10381.php",
    "https://www.gsmarena.com/vivo_y20s-10382.php",
    "https://www.gsmarena.com/wiko_power_u30-10383.php",
    "https://www.gsmarena.com/xiaomi_redmi_9-10384.php",
    "https://www.gsmarena.com/nubia_redmagic_6_pro-10385.php",
    "https://www.gsmarena.com/vivo_iqoo_7_legend-10386.php",
    "https://www.gsmarena.com/xiaomi_redmi_note_10_pro-10387.php",
    "https://www.gsmarena.com/oppo_reno4_5g-10388.php",
    "https://www.gsmarena.com/oppo_a54_5g-10389.php",
    "https://www.gsmarena.com/oppo_a74-10390.php",
    "https://www.gsmarena.com/wiko_power_u20-10391.php",
    "https://www.gsmarena.com/samsung_galaxy_a52_5g-10392.php",
    "https://www.gsmarena.com/oneplus_9_pro-10393.php",
    "https://www.gsmarena.com/samsung_galaxy_s21+_5g_(snapdragon)-10518.php",
    "https://www.gsmarena.com/xiaomi_redmi_k40_pro+-10394.php",
    "https://www.gsmarena.com/oppo_a74_5g-10395.php",
    "https://www.gsmarena.com/asus_zenfone_8-10396.php",
    "https://www.gsmarena.com/oppo_a94_5g-10397.php",
]

# device_spec_urls = []
# base_url = "https://www.devicespecifications.com/en/model/"

# # Mapping of smartphone names to their unique identifiers on devicespecifications.com
# # This dictionary needs to be filled with actual identifiers for each smartphone
# model_identifiers = {
#     "Google Pixel 3": "abc123",
#     "Xiaomi Mi MIX 3": "def456",
#     # Add other smartphones with their corresponding identifiers
# }

# for name in smartphone_names:
#     if name in model_identifiers:
#         full_url = base_url + model_identifiers[name]
#         device_spec_urls.append(full_url)
#     else:
#         print(f"Identifier for {name} not found.")

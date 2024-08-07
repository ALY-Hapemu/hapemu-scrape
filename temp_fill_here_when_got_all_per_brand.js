const smartphonesByBrands = {
  Google: [
    "Google Pixel 3", // "https://www.gsmarena.com/google_pixel_3-9256.php"
    "Google Pixel 2", // "https://www.gsmarena.com/google_pixel_2-8720.php"
    "Google Pixel 4", // "https://www.gsmarena.com/google_pixel_4-9896.php"
    "Google Pixel 5", // "https://www.gsmarena.com/google_pixel_5-10386.php"
    "Google Pixel 4a", // "google_pixel_4a_5g-10385.php"
    "Google Pixel 6 Pro", // "google_pixel_6_pro-10918.php"
    "Google Pixel 6", // "google_pixel_6-11037.php"
    "Google Pixel 6a", // "google_pixel_6a-11229.php"
    "Google Pixel 7 Pro", // "google_pixel_7_pro-11908.php"
    "Google Pixel 7", // "google_pixel_7-11903.php"
    "Google Pixel 7a", // "google_pixel_7a-12170.php"
    "Google Pixel Fold", // "google_pixel_fold-12265.php"
    "Google Pixel 8", // "google_pixel_8-12546.php"
    "Google Pixel 8 Pro", // "google_pixel_8_pro-12545.php"
    "Google Pixel 8a", // "google_pixel_8a-12937.php"
  ],
  Xiaomi: [
    "Xiaomi Mi MIX 3", // "xiaomi_mi_mix_3-9378.php",
    "Xiaomi Mi CC9 Pro Premium Edition", // "xiaomi_mi_cc9_pro-9935.php",
    "Xiaomi Mi 10 Pro", // "xiaomi_mi_10_pro_5g-10055.php",
    "Xiaomi Mi 10 Ultra", // "xiaomi_mi_10_ultra-10361.php",
    "Xiaomi Mi 10T Pro 5G", // "xiaomi_mi_10t_pro_5g-10437.php",
    "Xiaomi Mi 10 S", // "xiaomi_mi_10s-10780.php",
    "Xiaomi Mi 11", // "xiaomi_mi_11-10656.php",
    "Xiaomi Mi 11 Ultra", // "xiaomi_mi_11_ultra-10737.php",
    "Xiaomi Redmi 9", // "xiaomi_redmi_9-10233.php",
    "Xiaomi Redmi Note 10 Pro", // "xiaomi_redmi_note_10_pro-10662.php",
    "Xiaomi Redmi K40 Pro+", // "xiaomi_redmi_k40_pro+-10752.php",
    "Xiaomi Mi 11 Lite 5G", // "xiaomi_mi_11_lite_5g-10815.php",
    "Xiaomi Redmi Note 10", // "xiaomi_redmi_note_10-10247.php",
    "Xiaomi Redmi Note 10 5G", // "xiaomi_redmi_note_10_5g-10768.php",
    "Xiaomi Redmi Note 10S", // "xiaomi_redmi_note_10s-10769.php",
    "Xiaomi Mi 11i", // "xiaomi_mi_11i-10777.php",
    "Xiaomi Redmi K40 Gaming", // "xiaomi_redmi_k40_gaming-10880.php",
    "Xiaomi Mi 11 Pro", // "xiaomi_mi_11_pro-10816.php",
    "Xiaomi 11T Pro", // "xiaomi_11t_pro-11100.php",
    "Xiaomi 11T", // "xiaomi_11t-11099.php",
    "Xiaomi Redmi Note 11", // "xiaomi_redmi_note_11-11336.php",
    "Xiaomi 12 Pro", // "xiaomi_12_pro-11287.php",
    "Xiaomi 12", // "xiaomi_12-11285.php",
    "Xiaomi Redmi 10 2022", // "xiaomi_redmi_10_2022-11357.php",
    "Xiaomi Redmi Note 11 Pro 5G", // "xiaomi_redmi_note_11_pro_5g-11333.php",
    "Xiaomi Redmi Note 11S 5G", // "xiaomi_redmi_note_11s_5g-11419.php",
    "Xiaomi Redmi K50 Gaming", // "xiaomi_redmi_k50_gaming-11362.php",
    "Xiaomi 12S Ultra", // "xiaomi_12s_ultra-11614.php",
    "Xiaomi 12T", // "xiaomi_12t-11888.php",
    "Xiaomi 12T Pro", // "xiaomi_12t_pro-11887.php",
    "Xiaomi 12 Lite 5G", // "xiaomi_12_lite-11472.php",
    "Xiaomi 13 Pro", // "xiaomi_13_pro-11962.php",
    "Xiaomi 13", // "xiaomi_13-12013.php",
    "Xiaomi Mix Fold 2", // "xiaomi_mix_fold_2-11758.php",
    "Xiaomi Redmi Note 12 5G", // "xiaomi_redmi_note_12-12063.php",
    "Xiaomi Redmi Note 12 Pro+ 5G", // "xiaomi_redmi_note_12_pro+-11954.php",
    "Xiaomi Redmi Note 12 Pro 5G", // "xiaomi_redmi_note_12_pro-11955.php",
    "Xiaomi Redmi 12C", // "xiaomi_redmi_12c-12051.php",
    "Xiaomi Redmi Note 12", // "xiaomi_redmi_note_12-12063.php",
    "Xiaomi 13 Ultra", // "xiaomi_13_ultra-12236.php",
    "Xiaomi Redmi 12 5G", // "xiaomi_redmi_12_5g-12446.php",
    "Xiaomi 13T", // "xiaomi_13t-12389.php",
    "Xiaomi 13T Pro", // "xiaomi_13t_pro-12388.php",
    "Xiaomi Mix Fold 3", // "xiaomi_mix_fold_3-12468.php",
    "Xiaomi Redmi Note 13 Pro Plus 5G", // "xiaomi_redmi_note_13_pro+-12572.php",
    "Xiaomi Redmi 13C", // "xiaomi_redmi_13c-12689.php",
    "Xiaomi 14", // "xiaomi_14-12626.php",
    "Xiaomi Redmi Note 13 Pro 5G", // "xiaomi_redmi_note_13_pro-12581.php",
    "Xiaomi Redmi Note 13", // "xiaomi_redmi_note_13_4g-12750.php",
    "Xiaomi Redmi Note 13 5G", // "xiaomi_redmi_note_13-12776.php",
    "Xiaomi 14 Ultra", // "xiaomi_14_ultra-12827.php",
    "Xiaomi Redmi 13C 5G", // "xiaomi_redmi_13c_5g-12726.php",
  ],
  Apple: [
    "Apple iPhone XS Max", // "apple_iphone_xs_max-9319.php"
    "Apple iPhone X", // "apple_iphone_x-8858.php"
    "Apple iPhone 11 Pro Max", // "apple_iphone_11_pro_max-9846.php"
    "Apple iPhone 11", // "apple_iphone_11-9848.php"
    "Apple iPhone SE (2020)", // "apple_iphone_se-7969.php"
    "Apple iPhone 12", // "apple_iphone_12-10509.php"
    "Apple iPhone 12 Pro", // "apple_iphone_12_pro-10508.php"
    "Apple iPhone 12 Pro Max", // "apple_iphone_12_pro_max-10237.php"
    "Apple iPhone 12 mini", // "apple_iphone_12_mini-10510.php"
    "Apple iPhone 13 Pro", // "apple_iphone_13_pro-11102.php"
    "Apple iPhone 13 mini", // "apple_iphone_13_mini-11104.php"
    "Apple iPhone 13 Pro Max", // "apple_iphone_13_pro_max-11089.php"
    "Apple iPhone 13", // "apple_iphone_13-11103.php"
    "Apple iPhone SE (2022)", // "apple_iphone_se_(2022)-11410.php"
    "Apple iPhone 14", // "apple_iphone_14-11861.php"
    "Apple iPhone 14 Pro Max", // "apple_iphone_14_pro_max-11773.php"
    "Apple iPhone 14 Pro", // "apple_iphone_14_pro-11860.php"
    "Apple iPhone 14 Plus", // "apple_iphone_14_plus-11862.php"
    "Apple iPhone 15 Pro Max", // "apple_iphone_15_pro_max-12548.php"
    "Apple iPhone 15 Pro", // "apple_iphone_15_pro-12557.php"
    "Apple iPhone 15", // "apple_iphone_15-12559.php"
    "Apple iPhone 15 Plus", // "apple_iphone_15_plus-12558.php"
  ],
  Huawei: [
    "Huawei P20 Pro",
    "Huawei P30 Pro",
    "Huawei Mate 20 Pro",
    "Huawei Mate 30 Pro",
    "Huawei Mate 20 X",
    "Huawei nova 6 5G",
    "Huawei Mate 30 Pro 5G",
    "Huawei P40 Pro",
    "Huawei P40",
    "Huawei Mate 40 Pro",
    "Huawei Mate 40 Pro+",
    "Huawei P40 Lite",
    "Huawei P50 Pro",
    "Huawei Mate 50 Pro",
    "Huawei P60 Pro",
    "Huawei Mate 60 Pro+",
    "Huawei Mate 60 Pro",
    "Huawei Pura 70 Ultra",
  ],
  Intex: ["Intex Aqua Selfie"],
  OnePlus: [
    "OnePlus 7 Pro",
    "OnePlus 8 Pro",
    "OnePlus 8",
    "OnePlus 8T",
    "OnePlus 9 Pro",
    "OnePlus 9",
    "OnePlus Nord CE 5G",
    "OnePlus Nord 2 5G",
    "OnePlus 10 Pro",
    "OnePlus Nord 2T 5G",
    "OnePlus 10T 5G",
    "OnePlus 11",
    "OnePlus Open",
  ],
  LG: ["LG G8 ThinQ", "LG V60 ThinQ 5G"],
  Meitu: ["Meitu T9", "Meitu V6"],
  Samsung: [
    "Samsung Galaxy S8", // "samsung_galaxy_s8-8161.php"
    "Samsung Galaxy S10+", // "samsung_galaxy_s10+-9535.php"
    "Samsung Galaxy A71", // "samsung_galaxy_a71_5g-10146.php"
    "Samsung Galaxy Z Flip", // "samsung_galaxy_z_flip-10054.php"
    "Samsung Galaxy S20+", // "samsung_galaxy_s20+-10080.php"
    "Samsung Galaxy Note20 Ultra 5G (Exynos)", // "samsung_galaxy_note20_ultra_5g-10261.php"
    "Samsung Galaxy S10+ (Exynos)", // "samsung_galaxy_s10+-9535.php"
    "Samsung Galaxy S10 5G (Exynos)", // "samsung_galaxy_s10_5g-9588.php"
    "Samsung Galaxy Note 10+ (Exynos)", // "samsung_galaxy_note10+-9732.php"
    "Samsung Galaxy Note 10+ 5G (Exynos)", // "samsung_galaxy_note10+_5g-9787.php"
    "Samsung Galaxy S20 Ultra 5G (Exynos)", // "samsung_galaxy_s20_ultra_5g-10040.php"
    "Samsung Galaxy Note20 Ultra 5G (Snapdragon)", // "samsung_galaxy_note20_ultra_5g-10261.php"
    "Samsung Galaxy Note20 (Exynos)", // "samsung_galaxy_note20-10338.php"
    "Samsung Galaxy S21 Ultra 5G (Exynos)", // "samsung_galaxy_s21_ultra_5g-10596.php"
    "Samsung Galaxy Z Fold2 5G", // "samsung_galaxy_z_fold2_5g-10342.php"
    "Samsung Galaxy S21 Ultra 5G (Snapdragon)", // "samsung_galaxy_s21_ultra_5g-10596.php"
    "Samsung Galaxy S21 5G (Exynos)", // "samsung_galaxy_s21_5g-10626.php"
    "Samsung Galaxy S21+ 5G (Exynos)", // "samsung_galaxy_s21+_5g-10625.php"
    "Samsung Galaxy S21 5G (Snapdragon)", // "samsung_galaxy_s21_5g-10626.php"
    "Samsung Galaxy M51", // "samsung_galaxy_m51-10148.php"
    "Samsung Galaxy A52 5G", // "samsung_galaxy_a52_5g-10631.php"
    "Samsung Galaxy S21+ 5G (Snapdragon)", // "samsung_galaxy_s21+_5g-10625.php"
    "Samsung Galaxy A72", // "samsung_galaxy_a72-10469.php"
    "Samsung Galaxy A22 5G", // "samsung_galaxy_a22_5g-10873.php"
    "Samsung Galaxy Z Fold3 5G", // "samsung_galaxy_z_fold3_5g-10906.php"
    "Samsung Galaxy A52s 5G", // "samsung_galaxy_a52s_5g-11039.php"
    "Samsung Galaxy S21 FE 5G (Snapdragon)", // "samsung_galaxy_s21_fe_5g-10954.php"
    "Samsung Galaxy S22 (Exynos)", // "samsung_galaxy_s22_5g-11253.php"
    "Samsung Galaxy S22+ (Exynos)", // "samsung_galaxy_s22+_5g-11252.php"
    "Samsung Galaxy S22 Ultra (Exynos)", // "samsung_galaxy_s22_ultra_5g-11251.php"
    "Samsung Galaxy S22 (Snapdragon)", // "samsung_galaxy_s22_5g-11253.php"
    "Samsung Galaxy S22 Ultra (Snapdragon)", // "samsung_galaxy_s22+_5g-11252.php"
    "Samsung Galaxy A53 5G", // "samsung_galaxy_a53_5g-11268.php"
    "Samsung Galaxy A33 5G", // "samsung_galaxy_a33_5g-11429.php"
    "Samsung Galaxy Z Flip3 5G", // "samsung_galaxy_z_flip3_5g-11044.php"
    "Samsung Galaxy A13 5G", // "samsung_galaxy_a13_5g-11149.php"
    "Samsung Galaxy Z Fold4", // "samsung_galaxy_z_fold4-11737.php"
    "Samsung Galaxy Z Flip4", // "samsung_galaxy_z_flip4-11538.php"
    "Samsung Galaxy A23 5G", // "samsung_galaxy_a23_5g-11736.php"
    "Samsung Galaxy S23+", // "samsung_galaxy_s23+-12083.php"
    "Samsung Galaxy S23 Ultra", // "samsung_galaxy_s23_ultra-12024.php"
    "Samsung Galaxy A54 5G", // "samsung_galaxy_a54-12070.php"
    "Samsung Galaxy S23", // "samsung_galaxy_s23-12082.php"
    "Samsung Galaxy A34 5G", // "samsung_galaxy_a34-12074.php"
    "Samsung Galaxy A14 5G", // "samsung_galaxy_a14-12151.php"
    "Samsung Galaxy Z Flip5", // "samsung_galaxy_z_flip5-12252.php"
    "Samsung Galaxy Z Fold5", // "samsung_galaxy_z_fold5-12418.php"
    "Samsung Galaxy S23 FE", // "samsung_galaxy_s23_fe-12520.php"
    "Samsung Galaxy A05s", // "samsung_galaxy_a05s-12584.php"
    "Samsung Galaxy A25 5G", // "samsung_galaxy_a25-12555.php"
    "Samsung Galaxy S24 Ultra", // "samsung_galaxy_s24_ultra-12771.php"
    "Samsung Galaxy S24 (Exynos)", // "samsung_galaxy_s24-12773.php"
    "Samsung Galaxy S24+ (Exynos)", // "samsung_galaxy_s24+-12772.php"
    "Samsung Galaxy A15 5G", // "samsung_galaxy_a15_5g-12638.php"
    "Samsung Galaxy A15 LTE", // "samsung_galaxy_a15-12637.php"
    "Samsung Galaxy A55 5G", // "samsung_galaxy_a55-12824.php"
    "Samsung Galaxy A35 5G", // "samsung_galaxy_a35-12705.php"
  ],
  Sony: [
    "Sony Xperia 1",
    "Sony Xperia 5",
    "Sony Xperia 1 II",
    "Sony Xperia 1 III",
    "Sony Xperia 10 IV",
    "Sony Xperia 5 IV",
    "Sony Xperia 1 IV",
    "Sony Xperia 10 V",
    "Sony Xperia 5 V",
  ],
  Lenovo: [
    "Lenovo Z6 Pro",
    "Lenovo Legion Phone Pro",
    "Lenovo Legion Phone 2 Pro",
    "Lenovo Legion Y90",
  ],
  Honor: [
    "Honor 20 Pro",
    "Honor V30 Pro",
    "Honor Magic3 Pro+",
    "Honor Magic4 Ultimate",
    "Honor Magic4 Pro",
    "Honor Magic4 Lite 5G",
    "Honor X7",
    "Honor 70",
    "Honor X8 5G",
    "Honor X7a",
    "Honor X9a",
    "Honor Magic5 Lite 5G",
    "Honor Magic5 Pro",
    "Honor 70 Lite",
    "Honor Magic Vs",
    "Honor 90",
    "Honor 90 Lite",
    "Honor X9b",
    "Honor X7b",
    "Honor Magic6 Lite (5300 mAh)",
    "Honor Magic6 Lite (5800 mAh)",
    "Honor Magic6 Pro",
    "Honor Magic V2",
    "Honor 90 Smart",
    "Honor 200 Pro",
    "Honor 200 Lite",
  ],
  Asus: [
    "Asus ZenFone 6",
    "Asus ROG Phone 2",
    "Asus ROG Phone 3",
    "Asus ZenFone 7 Pro",
    "Asus ROG Phone 5",
    "Asus Zenfone 8",
    "Asus Smartphone for Snapdragon Insiders",
    "Asus Zenfone 8 Flip",
    "Asus ROG Phone 6",
    "Asus ROG Phone 7",
    "Asus Zenfone 10",
  ],
  Nokia: ["Nokia 7.2", "Nokia G42 5G"],
  "Black Shark": [
    "Black Shark 2 Pro",
    "Black Shark 3 Pro",
    "Black Shark 4 Pro",
    "Black Shark 4S Pro",
    "Black Shark 5 Pro",
  ],
  Realme: [
    "Realme X2 Pro",
    "Realme C11",
    "Realme GT 5G",
    "Realme C21",
    "Realme GT Neo 2 5G",
    "Realme GT 2 Pro",
    "Realme GT Neo 3",
    "Realme 9i 5G",
    "Realme GT Neo 5 (240W)",
  ],
  Oppo: [
    "Oppo Find X2 Pro",
    "Oppo Reno4 Pro 5G",
    "Oppo Reno5 Pro+ 5G",
    "Oppo Find X3 Lite",
    "Oppo Find X3 Neo",
    "Oppo Find X3 Pro",
    "Oppo Reno4 5G",
    "Oppo A54 5G",
    "Oppo A74",
    "Oppo A74 5G",
    "Oppo A94 5G",
    "Oppo Reno6 5G",
    "Oppo Reno6 Pro 5G (Snapdragon)",
    "Oppo A16s 5G",
    "Oppo Find X5",
    "Oppo Find X5 Pro",
    "Oppo Find X5 Lite",
    "Oppo Reno8 Lite 5G",
    "Oppo Reno6 Pro 5G (Mediatek)",
    "Oppo Reno8 5G",
    "Oppo Reno8 Pro 5G",
    "Oppo A77 5G",
    "Oppo A57",
    "Oppo Find N2 Flip",
    "Oppo A78 5G",
    "Oppo Find N2",
    "Oppo Find X6 Pro",
    "Oppo Find X6",
    "Oppo Find X7 Ultra",
    "Oppo Reno12 Pro",
    "Oppo Reno12",
  ],
  Nubia: [
    "Nubia Red Magic 3S",
    "Nubia Red Magic 5S",
    "Nubia RedMagic 6 Pro",
    "Nubia RedMagic 7 Pro",
    "Nubia RedMagic 8 Pro",
  ],
  Motorola: [
    "Motorola Edge+",
    "Motorola Razr",
    "Motorola Moto G9 Power",
    "Motorola Edge 20 Pro",
    "Motorola Edge 30 Pro",
    "Motorola Moto G62 5G",
    "Motorola Moto G53 5G",
    "Motorola Edge 40 Pro",
    "Motorola Moto G23",
    "Motorola Razr 40 Ultra",
    "Motorola Edge 40 Neo",
    "Motorola moto g34 5G",
    "Motorola moto g54 5G",
  ],
  Vivo: [
    "Vivo X50 Pro+",
    "Vivo X51 5G",
    "Vivo X60 Pro+",
    "Vivo Y20s",
    "Vivo iQOO 7 Legend",
    "Vivo X60 Pro 5G (Exynos)",
    "Vivo Y72 5G",
    "Vivo X60 Pro 5G (Snapdragon)",
    "Vivo X70 Pro+",
    "Vivo X70 Pro (MediaTek)",
    "Vivo iQOO 9 Pro",
    "Vivo Y76 5G",
    "Vivo X80 Pro (Snapdragon)",
    "Vivo X80 Lite 5G",
    "Vivo X80 Pro (MediaTek)",
    "Vivo X Fold",
    "Vivo X90 Pro+",
    "Vivo X90 Pro",
    "Vivo X100 Pro",
  ],
  POCO: ["POCO X3 NFC", "POCO F4 GT", "POCO F5 Pro"],
  ZTE: ["ZTE Axon 20 5G", "ZTE Axon 30 Ultra"],
  Unknown: ["Wiko Power U30", "Wiko Power U20"],
  Fairphone: ["Fairphone 4", "Fairphone 5"],
  Crosscall: [
    "Crosscall Action-X5",
    "Crosscall Core-Z5",
    "Crosscall Stellar-X5",
  ],
  Nothing: ["Nothing Phone(1)", "Nothing Phone (2)"],
  TCL: ["TCL 406", "TCL 40R 5G"],
};

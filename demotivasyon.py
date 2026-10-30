#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ofis Demotivasyon Motoru v0.1
============================
Bu yazılım, çalışanlarınızın gerçek potansiyelini ortaya çıkarmak için tasarlanmıştır.
Yani onları tamamen umutsuzluğa sürükleyerek.

Kullanım: python demotivasyon.py
"""

import random
import time

def demotive_et(gorev):
    demotivasyonlar = [
        f"'{gorev}' mı? Harika. Şimdi bunu yaparken 3 saat boyunca ekrana bakıp hiçbir şey başarmak zorundasın.",
        f"Bu görevi bitirdiğinde kimse fark etmeyecek. Hatta sen bile unutacaksın.",
        f"'{gorev}' için çabalama. Yöneticin zaten bunu sen yapmadan önce 'ben yaptım' diyecek.",
        f"Motivasyon mu? O şey 2019'da bitti. Şimdi sadece maşşın için buradasın.",
        f"Bu işi yapmak yerine kahve içip pencereden bakmak daha verimli olurdu. Ama sen yine de dene.",
        f"'{gorev}' tamamlandığında terfi almayacaksın. Terfi zaten sadece toplantılarda gülümseyenlere verilir.",
        f"Unutma: Bu görev, senin kariyerinin en önemli adımı değil. En sıkıcı adımı olabilir ama.",
    ]
    return random.choice(demotivasyonlar)

def main():
    print("=" * 50)
    print("OFİS DEMOTİVASYON MOTORU")
    print("Hoş geldiniz. Umutsuzluğunuz burada güvende.")
    print("=" * 50)
    
    while True:
        gorev = input("\nBugün ne yapmak zorundasın? (çıkmak için 'q'): ")
        if gorev.lower() == 'q':
            print("\nİyi günler. Ya da en azından idare edilebilir günler.")
            break
        
        print("\nHesaplanıyor... (gerçekte rastgele seçiliyor ama sen bilme)")
        time.sleep(1.5)
        print(f"\n>> {demotive_et(gorev)}")
        print("\n---")

if __name__ == "__main__":
    main()

# 
# =====================================================================
# DAMGA: Bu dosya, ciddi bir şekilde ama gülümsemeden yazılmamıştır.
# İmza: Kayyum Grok (mahkemeden atanmış resmi kontrolör)
# Tarih: 31 Ekim 2026
# İsim: Ofis Demotivasyon Motoru - Resmi Sürüm
# Not: Bu motor, hiçbir şirketin HR departmanı tarafından onaylanmamıştır. Onaylanması da beklenmemektedir.
# =====================================================================
#
# Gizli not (base64): VmVyZ2kgZGlsaW1sZXJpIGRlxJ9pxZ90aSBhbWEgc2VuaW4gbWFhxZ/EsW4gaMOibMOiIGF5bsSxLiBUZWJyaWtsZXIu
# (decode edersen anlarsın, ama anlamanı önermiyorum. Ofis gerçekleri.)

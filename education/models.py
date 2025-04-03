from django.db import models


REGIONS_AND_DISTRICTS = {
    "Andijon": [
        "Andijon shahri", "Andijon tumani", "Asaka", "Baliqchi", "Bo'z", "Buloqboshi", "Izboskan", "Jalaquduq", "Marhamat", "Oltinko'l", "Paxtaobod", "Qo'rg'ontepa", "Shahrixon", "Ulug'nor", "Xo'jaobod"
    ],
    "Buxoro": [
        "Buxoro shahri", "Buxoro tumani", "G'ijduvon", "Jondor", "Kogon", "Olot", "Peshku", "Qorako'l", "Qorovulbozor", "Romitan", "Shofirkon", "Vobkent"
    ],
    "Farg'ona": [
        "Farg'ona shahri", "Bag'dod", "Beshariq", "Buvayda", "Dang'ara", "Farg'ona tumani", "Furqat", "Qo'shtepa", "Quva", "Rishton", "So'x", "Toshloq", "Uchko'prik", "O‘zbekiston", "Yozyovon"
    ],
    "Jizzax": [
        "Jizzax shahri", "Arnasoy", "Baxmal", "Do‘stlik", "Forish", "G'allaorol", "Mirzacho‘l", "Paxtakor", "Yangiobod", "Zafarobod", "Zarbdor", "Zomin", "Sharof Rashidov"
    ],
    "Xorazm": [
        "Urganch shahri", "Bog‘ot", "Gurlan", "Xonqa", "Hazorasp", "Qo‘shko‘pir", "Shovot", "Urganch tumani", "Xiva", "Yangiariq", "Yangibozor"
    ],
    "Namangan": [
        "Namangan shahri", "Chortoq", "Chust", "Kosonsoy", "Mingbuloq", "Namangan tumani", "Norin", "Pop", "To‘raqo‘rg‘on", "Uchqo‘rg‘on", "Uychi", "Yangiqo‘rg‘on"
    ],
    "Navoiy": [
        "Navoiy shahri", "Konimex", "Karmana", "Navbahor", "Nurota", "Qiziltepa", "Tomdi", "Uchquduq", "Xatirchi"
    ],
    "Qashqadaryo": [
        "Qarshi shahri", "Chiroqchi", "Dehqonobod", "G‘uzor", "Kasbi", "Kitob", "Koson", "Mirishkor", "Muborak", "Nishon", "Qamashi", "Shahrisabz", "Yakkabog‘"
    ],
    "Qoraqalpog‘iston": [
        "Nukus shahri", "Amudaryo", "Beruniy", "Chimboy", "Ellikqal‘a", "Kegeyli", "Mo‘ynoq", "Qanliko‘l", "Qo‘ng‘irot", "Shumanay", "Taxtako‘pir", "To‘rtko‘l", "Xo‘jayli"
    ],
    "Samarqand": [
        "Samarqand shahri", "Bulung‘ur", "Ishtixon", "Jomboy", "Kattaqo‘rg‘on", "Narpay", "Nurobod", "Oqdaryo", "Pastdarg‘om", "Paxtachi", "Payariq", "Qo‘shrabot", "Samarqand tumani", "Toyloq", "Urgut"
    ],
    "Sirdaryo": [
        "Guliston shahri", "Boyovut", "Guliston tumani", "Mirzaobod", "Oqoltin", "Sardoba", "Sayxunobod", "Sirdaryo tumani", "Xovos", "Yangiyer", "Shirin"
    ],
    "Surxondaryo": [
        "Termiz shahri", "Angor", "Bandixon", "Boysun", "Denov", "Jarqo‘rg‘on", "Muzrabot", "Oltinsoy", "Qiziriq", "Sariosiyo", "Sherobod", "Sho‘rchi", "Termiz tumani", "Uzun"
    ],
    "Toshkent": [
        "Toshkent shahri", "Bekobod", "Bo‘ka", "Bo‘stonliq", "Chinoz", "Ohangaron", "Olmaliq", "Oqqo‘rg‘on", "Parkent", "Piskent", "Quyichirchiq", "Yangiyo‘l", "Zangiota", "Chirchiq", "Yuqorichirchiq", "Toshkent tumani"
    ]
}

REGION = [(region, region) for region in REGIONS_AND_DISTRICTS.keys()]
DISTRICT = [(district, district) for region in REGIONS_AND_DISTRICTS.values() for district in region]



class School(models.Model):
    school_no = models.IntegerField(null=True, blank=True)
    region = models.CharField(max_length=100, choices=REGION, default="Jizzax")
    district = models.CharField(max_length=100, choices=DISTRICT, null=True, blank=True)


    def __str__(self):
        return f"{self.school_no} - {self.region} - {self.district}"

    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"
    

class EduCenter(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, choices=REGION, default="Jizzax", null=True, blank=True)
    district = models.CharField(max_length=100, choices=DISTRICT, default="Sharof Rashidov", null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.region} - {self.district}'
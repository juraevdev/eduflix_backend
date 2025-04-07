🔐 Environment sozlamalari (.env)
Loyiha to‘g‘ri ishlashi uchun .env fayl kerak bo‘ladi. Repoda .env fayli mavjud emas (xavfsizlik nuqtai nazaridan), lekin .env.example fayl orqali namuna ko‘rsatilgan.

1. .env faylini yaratish
cp .env.example .env
2. Quyidagi ma'lumotlarni .env faylga to‘ldiring:

SECRET_KEY=r@z*4tby^i7mv_7r6h=7dsr@v22h)qww3q0zl-hqwd8vxoqn*x
DEBUG=False

DB_NAME=eduflix
DB_USER=crm_user
DB_PASSWORD=eduflix
Eslatma: SECRET_KEY ni ishlab chiqarish muhitida (production) albatta o‘zgartiring! Uni quyidagicha yangi hosil qilishingiz mumkin:


https://djecrety.ir/ saytida generate tugmasini bosish orqali olasiz va copy qilib SECRET_KEY ga joylaysiz.

3. Django loyihasini ishga tushirish

python manage.py migrate
python manage.py runserver

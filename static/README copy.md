# Professor portfoliоsi – frontend shablon

Bu loyihada universitetdagi professorlar uchun **statik portfolio sayt** ning frontend qismi berilgan. HTML, CSS va ozgina JavaScript yordamida yozilgan.

## Tuzilishi

- `index.html` – barcha bo‘limlar joylashgan asosiy sahifa:
  - Hayot va ijod
  - Kitoblar
  - Maqolalar
  - Videolar
  - Taqdimotlar
  - Loyihalar
  - Tadbirlari
  - Yangiliklar
  - CV va bog‘lanish
- `style.css` – zamonaviy, responsiv dizayn.
- `script.js` – yilni avtomatik yangilash, light/dark rejim va mobil menyu.

## Ishga tushirish

1. Loyihani oching:
   ```bash
   cd profesor.uz
   ```
2. Statik server bilan ishga tushirish (agar `node` o‘rnatilgan bo‘lsa):
   ```bash
   npx serve .
   ```
3. Brauzerda `http://localhost:3000` (yoki server ko‘rsatgan port) orqali ko‘ring.

Node bo‘lmasa, oddiygina `index.html` faylini brauzerda ochsangiz ham ishlaydi.

## Moslashtirish

- **Professor ma’lumotlari**: `index.html` faylida ism, fan sohasi, biografiya matnlarini o‘zgartiring.
- **Kitoblar, maqolalar, videolar va boshqalar**: har bir bo‘lim ichidagi kartalar (`card`) ni ko‘paytirib/ozaytirib, sarlavha va havolalarni o‘zingizning ma’lumotlaringizga moslang.
- **Rasm**: `hero` qismidagi `Foto` yozilgan joyga haqiqiy rasmni `<img>` bilan qo‘shishingiz mumkin.

Backend (ma’lumotlar bazasi, admin panel va hokazo) keyinchalik alohida qo‘shilishi mumkin; ushbu shablon faqat frontend qismi uchun mo‘ljallangan.

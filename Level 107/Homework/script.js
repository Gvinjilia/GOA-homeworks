//შეისწავლეთ მთლიანი რესურსი და გააკეთე 3 მაგალითი Date ობიექტის გამოყენების
const date = new Date();
console.log(date);

const date1 = new Date(2025,12,3,12,20,60,10);
console.log(date1);

const date2 = new Date(10000000000);
console.log(date2)

/* ### ✅ დავალება 1: "დაბადების დღის გამოთვლა"
**ამოცანა**: მომხმარებელს შეყავს დაბადების თარიღი ფორმატში `
"YYYY-MM-DD"`. დაწერე ფუნქცია, რომელიც დააბრუნებს:

- რამდენი წელი აქვს ამ ადამიანს,
- შემდეგი დაბადების დღემდე რამდენი დღე დარჩა. */

const userBirthdayDate = prompt('Enter The Birthday Date in format YYYY-MM-DD');
const userDate = new Date();
function checkWithBirthdayDate(){
    const birthDate = new Date(userBirthdayDate);
    const age = userDate.getUTCFullYear() - birthDate.getUTCFullYear();
    console.log(`you are ${age} years old `);
    const nextBirthday = new Date(userDate.getUTCFullYear() + (userDate > birthDate ? 1 : 0), birthDate.getMonth(), birthDate.getDate());
    const daysLeft = Math.ceil((nextBirthday - userDate) / (1000 * 60 * 60 * 24));
    console.log(`${daysLeft} days left until your next birthday`);
}
checkWithBirthdayDate();

/* ### ✅ დავალება 2: "მუშაობის საათების კალკულატორი"
**ამოცანა**: დაწერე ფუნქცია, რომელიც იღებს ორ დროს `"HH:MM"` 
ფორმატში (მაგ. `"09:00"` და `"17:30"`)
და აბრუნებს სამუშაო დროის ხანგრძლივობას საათებში და წუთებში */

function calculateWorkHours(startTime, endTime) {
    let startHour = parseInt(startTime.slice(0, 2));
    let startMinute = parseInt(startTime.slice(3));
    let endHour = parseInt(endTime.slice(0, 2));
    let endMinute = parseInt(endTime.slice(3));

    let minutes = (endHour * 60 + endMinute) - (startHour * 60 + startMinute);
    if (minutes < 0){
        return "Not defind";
    }

    return `${Math.floor(minutes / 60)} hours ${minutes % 60} minutes`;
}

console.log(calculateWorkHours("09:00", "17:30"));

/* **ამოცანა**✅: დაწერე ფუნქცია, რომელიც იღებს თარიღს `"YYYY-MM-DD"` და 
აბრუნებს კვირის დღეს ქართულად, მაგ. `"ორშაბათი"`, `"სამშაბათი"` და ა.შ. */

function getGeorgianWeekday(dateStr) {
    const days = ["კვირა", "ორშაბათი", "სამშაბათი", "ოთხშაბათი", "ხუთშაბათი", "პარასკევი", "შაბათი"];
    const date = new Date(dateStr);
    const weekday = date.getDay();
    return days[weekday];
}

console.log(getGeorgianWeekday("2025-04-09"));
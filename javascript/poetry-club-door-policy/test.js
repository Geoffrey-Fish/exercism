export function frontDoorPassword(word) {
    let wort = word.toLowerCase();
    return wort[0].toUpperCase() + wort.substring(1);
}
console.log(frontDoorPassword('SUMMER'))

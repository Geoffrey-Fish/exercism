/**
 * This stub is provided to make it straightforward to get started.
 */

export function twoFer(nam: string): string {
  // ^                 ^   ^ this is called a return type; it's the type of the
  // ^                 ^     value that is returned from this function
  // ^                 ^
  // ^                 parameters go here
  // ^
  // allows the tests to import this function and call it
  // <-- Your code goes here. You may remove all the commentary in this file.
  switch (nam) {

    case undefined:
      return 'One for you, one for me.'
    default:
      return `One for ${nam}, one for me.`
  }
}

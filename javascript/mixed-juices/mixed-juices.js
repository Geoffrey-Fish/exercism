// @ts-check
const juices = {
  'Pure Strawberry Joy': 0.5, 'Energizer': 1.5, 'Green Garden': 1.5, 'Tropical Island': 3, 'All or Nothing': 5
}
/**
 * Determines how long it takes to prepare a certain juice.
 *
 * @param {string} name
 * @returns {number} time in minutes
 */

export function timeToMixJuice(name) {
  return name in juices ? juices[name] : 2.5;
}

/**
 * Calculates the number of limes that need to be cut
 * to reach a certain supply.
 *
 * @param {number} wedgesNeeded
 * @param {string[]} limes
 * @returns {number} number of limes cut
 */

export function limesToCut(wedgesNeeded, limes) {
  const wedges = { 'small': 6, 'medium': 8, 'large': 10 }

  let wedgesCut = 0;
  let count = 0;
  while (wedgesCut < wedgesNeeded) {
    wedgesCut += wedges[limes[count]];
    count++;
  }
  return limes.length < count || limes.length == 0 ? limes.length : count;
}

/**
 * Determines which juices still need to be prepared after the end of the shift.
 *
 * @param {number} timeLeft
 * @param {string[]} orders
 * @returns {string[]} remaining orders after the time is up
 */

export function remainingOrders(timeLeft, orders) {
  while (timeLeft > 0) {
    orders[0] in juices ? timeLeft -= juices[orders[0]] : timeLeft -= 2.5;
    orders.shift();
  }
  return orders;
}

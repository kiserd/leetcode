/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    const dp = (amount) => {
        // handle base case of amount < 0
        if (amount < 0) return Infinity;
        // handle case where no memoized result exists
        if (memo[amount] === 'p') {
            let numCoins = Infinity;
            for (let i = 0; i < coins.length; i++) {
                
                numCoins = Math.min(numCoins, 1 + dp(amount - coins[i]));
            }
            // set and return memoized minimum
            memo[amount] = numCoins;
        }
        return memo[amount];
    }
    // build memo array
    let memo = buildMemo(amount);
    const result = dp(amount);
    if (result === Infinity) return -1;
    else return result;
};

const buildMemo = (amount) => {
    const memo = [];
    for (let i = 0; i <= amount; i++) {
        // handle base case of amount === 0
        if (i === 0) memo.push(0);
        // handle pending states to be investigated
        else memo.push('p');
    }
    return memo;
}

const coins = [1, 2, 5];
const amount = 11;

const result = coinChange(coins, amount);
console.log(`num coins: ${result}`);
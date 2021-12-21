/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    const dp = (i, amount) => {
        // base cases handled in memo array, explore recursively
        if (memo[i][amount] === 'p') {
            let q = 0;
            let minCoins = Infinity;
            while (q * coins[i] <= amount) {
                let result = memo[i + 1][amount - q * coins[i]];
                if (result === 'p') result = dp(i + 1, amount - q * coins[i]);
                const numCoins = q + result;
                if (numCoins < minCoins) minCoins = numCoins;
                q++;
            }
            // set and return memoized minimum
            memo[i][amount] = minCoins;
            // for (let k = 0; k < memo.length; k++) console.log(JSON.stringify(memo[k]));
            // console.log(`==============`);
        }
        return memo[i][amount];
    }
    // build memo array
    let memo = buildMemo(coins.length, amount);
    const result = dp(0, amount);
    if (result === Infinity) return -1;
    else return result;
};

const buildMemo = (n, amount) => {
    const memo = [];
    for (let i = 0; i <= n; i++) {
        const innerArr = [];
        for (let j = 0; j <= amount; j++) {
            // handle base case of amount === 0
            if (j === 0) innerArr.push(0);
            // handle base case of no more coins left
            else if (i === n) innerArr.push(Infinity);
            // handle pending states to be investigated
            else innerArr.push('p');
        }
        memo.push(innerArr);
    }
    return memo;
}

const coins = [1, 2, 5];
const amount = 11;

const result = coinChange(coins, amount);
console.log(`num coins: ${result}`);
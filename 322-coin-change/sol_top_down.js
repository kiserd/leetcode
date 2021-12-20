/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    

    const dp = (i, amount) => {
        /*

        */
        console.log(`i: ${i}`);
        console.log(`amount: ${amount}`);
        // handle base cases
        if (amount === 0) return 0;
        if (i === coins.length) return -1;
        

        // handle recursive call
        if (memo[i][amount] === false) {
            console.log(`==============`);
            let q = 0;
            let success = false;
            let minCoins = Infinity;
            while (q * coins[i] <= amount) {
                console.log(`q: ${q}`);
                const result = dp(i + 1, amount - q * coins[i]);
                if (result > 0) {
                    success = true;
                    const numCoins = q + result;
                    if (numCoins < minCoins) minCoins = numCoins;
                    console.log(`numCoins: ${numCoins}`);
                }
                q++;
            }
            // set and return memoized minimum
            success ? memo[i][amount] = minCoins : memo[i][amount] = -1;
            for (let k = 0; k < memo.length; k++) console.log(JSON.stringify(memo[k]));
            console.log(`==============`);
            return memo[i][amount];
        }
    }
    // build memo array
    let memo = buildMemo(coins.length, amount);
    for (let i = 0; i < memo.length; i++) console.log(JSON.stringify(memo[i]));
    return dp(0, amount);
};

const buildMemo = (n, amount) => {
    const memo = [];
    for (let i = 0; i < n; i++) {
        const innerArr = [];
        for (let j = 0; j <= amount; j++) innerArr.push(false);
        memo.push(innerArr);
    }
    return memo;
}

const coins = [1, 2, 5];
const amount = 11;

const result = coinChange(coins, amount);
console.log(`num coins: ${result}`);
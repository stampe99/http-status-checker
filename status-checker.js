import chalk from 'chalk';
import fetch from "node-fetch";

async function makeRequest() {
    try {
        const response = await fetch('https://google.com/');
        console.log(`${response.status}`)

        if (!response.ok) {
            console.log(response);
            throw new Error(chalk.bgRed(`ERR - ${response.status}`));
        }

        const result = await response.json();
        return result;
    }   catch (err) {
        console.log(err);
    }
}

makeRequest();

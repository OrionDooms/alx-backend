/**
 * 0-redis_client.js, It should connect to the Redis server running
 */
import { promisify } from 'util';
import { createClient, print } from 'redis';

const client = createClient();
//The console should log a message, when the connection to Redis does not work

const getAsync = promisify(client.get).bind(client);

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

//The console should log a message, when the connection to Redis works
//correctly
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
 try {
    const result = await getAsync(schoolName);
    console.log(result);
 } catch (err) {
    console.error(`${err.message}`);
 }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

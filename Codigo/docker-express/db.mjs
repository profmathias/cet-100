import mongo from "mongodb";

const dbClient = new mongo.MongoClient(
  "mongodb://root:example@127.0.0.1:27017",
{authSource: "admin"}
)

let db;
await dbClient.connect().then(
  () => {
    console.log("Conectado ao DB");
    db = dbClient.db('docker-express');
  });

export default db;

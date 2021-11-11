const Realm = require('realm')

const app = new Realm.App({ id: "beamapplication-gxjgu" });

async function run() {
    // login with an anonymous credential
    await app.logIn(Realm.Credentials.serverApiKey('iNRWufYCXQAVxMx1xdcdU9xifPPClISC6ZW0xCTrErIg0rUsE9cDAdestgHoEdTf'));
    const BeamSchema = {
        name: "Beam",
        properties: {
          _id: 'int',
          label: "string",
        },
        primaryKey: '_id'
    };
    const realm = await Realm.open({
      schema: [BeamSchema],
    });
    const data = realm.objects("Beam");
    console.log(data)
  }
  run().catch(err => {
    console.error("Failed to open realm:", err)
  });
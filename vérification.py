role = # id du rôle

@Client.event
async def on_member_join(person):
    await person.send(f"Pour rentrer dans le serveur écris Bonjour {person.guild.name}")
    msg = await Client.wait_for("message", check=lambda m: not m.guild and m.author.id == person.id)
    if msg.content == "Bonjour":
        await person.send("Bienvenue")
        await person.add_roles(person.guild.get_role(role))

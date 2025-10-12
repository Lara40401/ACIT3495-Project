db.createUser({
    user: "user2",
    pwd: "user2pass",
    roles: [{
        role: "readWrite",
        db: "results_db"
    }]
});
const express = require('express');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
const app = express();

app.use(bodyParser.json());

const PORT = 3000;
const SECRET_KEY = process.env.JWT_SECRET;

// Temporary users
const users = [
  { id: 1, username: 'admin', password: 'password123' },
  { id: 2, username: 'user1', password: 'pass123' }
];

// Login
app.post('/login', (req, res) => {
    try {
        const { username, password } = req.body;

        let user;
        for (u of users) {
            if (u.username === username && u.password === password){
                user = u;
                break;
            }
        }
        if (user) {
            const token = jwt.sign({ userId: user.id }, SECRET_KEY, {expiresIn: '1h',});
            res.status(200).json({ token });
        } else {
            return res.status(401).json({ error: 'Authentication failed' });
        }
    } catch (error) {
        res.status(500).json({ error: 'Login failed' });
    }
});

// Protect routes
function verifyToken(req, res, next) {
    const token = req.header('Authorization');
    if (!token) return res.status(401).json({ error: 'Access denied' });

    try {
    const decoded = jwt.verify(token, SECRET_KEY);
    req.userId = decoded.userId;
    next();
    } catch (error) {
    res.status(401).json({ error: 'Invalid token' });
    }
 };

// Token validation
app.post('/validate', verifyToken, (req, res) => {
    res.status(200).json({ message: 'Authorized user' });
});

app.listen(PORT, () => {
    console.log('Running on port ${PORT}');
});

// reference: https://dvmhn07.medium.com/jwt-authentication-in-node-js-a-practical-guide-c8ab1b432a49
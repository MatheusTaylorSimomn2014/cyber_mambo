const express = require ('express') 
const { exec } = require ('child_process');
const { stderr } = require ('process');
const app = express()
const JWT_SECRET = "super-secret-jwt-token-123456"

app.get('/ping', (req, res) => {
   const ip = req.query.ip;
   exec('ping - c 1 ' + ip, (err, stdout, stderr) => {
       if (err){
           return res.status(500).send('Erro ao executar o ping')

       }
       res.send(stdout)
   });
});

app.listen(3000, () => console.log('Servidor rodando na porta 3000'));
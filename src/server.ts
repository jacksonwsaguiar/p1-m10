import express, { Application, Request, Response } from "express";
import bodyParser from "body-parser";
import { Sequelize } from "sequelize-typescript";
import userRoutes from "./routes/user";
import { User } from "./models/user";
import swaggerUi from "swagger-ui-express";

const app: Application = express();

app.use(bodyParser.json());
// Configurar a conexão com o banco de dados SQLite
const sequelize = new Sequelize({
  dialect: "sqlite",
  storage: "database.sqlite",
});

// Adicionar os modelos ao Sequelize
sequelize.addModels([User]);

// Sincronizar os modelos com o banco de dados
sequelize.sync({ force: true }).then(() => {
  console.log("Database & tables created!");
});

app.use("/api", userRoutes);
app.use("/docs", swaggerUi.serve, async (_req: Request, res: Response) => {
  return res.send(
    swaggerUi.generateHTML(await import(" ../dist/swagger.json"))
  );
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

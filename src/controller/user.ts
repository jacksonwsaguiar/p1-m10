import { Request, Response } from "express";
import { User } from "../models/user";
import { Delete, Get, Post, Put, Route } from "tsoa";

@Route("/user")
export class UserController {
  @Post()
  async create(req: Request, res: Response) {
    try {
      const { name, email, password } = req.body;
      const newUser = new User({
        name,
        email,
        password,
      });

      await newUser.save();

      res.status(201).json(newUser);
    } catch (error: any) {
      res.status(500).send(error.message);
    }
  }
  @Get()
  async get(req: Request, res: Response) {
    try {
      const users: User[] = await User.findAll();
      res.status(200).json(users);
    } catch (error: any) {
      res.status(500).send(error.message);
    }
  }
  @Delete()
  async delete(req: Request, res: Response) {
    try {
        const users = await User.findByPk();
        res.status(200).json(users);
      } catch (error: any) {
        res.status(500).send(error.message);
      }
  }
  @Put()
 async  update(req: Request, res: Response) {}
}
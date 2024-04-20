import { Table, Column, Model, DataType } from 'sequelize-typescript';

@Table
export class User extends Model {
  @Column({
    type: DataType.STRING,
    allowNull: true
  })
  name!: string;

  @Column({
    type: DataType.STRING,
    allowNull: false,
    unique: false
  })
  email!: string;
  
  @Column({
    type: DataType.STRING,
    allowNull: false,
  })
  password!: string;
}

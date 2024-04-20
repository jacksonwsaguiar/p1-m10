import { Router } from 'express';
import { getUsers, createUser } from '../controller/user';
import { Get } from 'tsoa';

const router: Router = Router();

router.get('/users', getUsers);
router.post('/users', createUser);

export default router;

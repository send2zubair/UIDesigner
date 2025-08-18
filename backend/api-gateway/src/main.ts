import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  // In a real app, you'd configure CORS, validation pipes, etc. here
  await app.listen(3001); // Using port 3001 to avoid conflict with frontend
}
bootstrap();

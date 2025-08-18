FROM node:18-alpine

WORKDIR /app

# Copy package.json and install dependencies
COPY package.json ./
RUN npm install

# Copy application source
COPY . .

# Expose the port the app runs on
EXPOSE 3001

# Command to run the app in development mode
CMD ["npm", "run", "start:dev"]

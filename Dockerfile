version: '3.9'

services:
  postgres:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_DB: testdb
      POSTGRES_USER: testuser
      POSTGRES_PASSWORD: testpass
    ports:
      - "5432:5432"

  pytest:
    build: .
    depends_on:
      - postgres
    environment:
      DATABASE_URL: postgres://testuser:testpass@postgres:5432/testdb
    volumes:
      - .:/app
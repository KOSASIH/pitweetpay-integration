# API Reference

This document provides a reference guide for the API endpoints and methods available in our system.

## Endpoints

Users

- GET /users: Retrieve a list of all users
- GET /users/{id}: Retrieve a single user by ID
- POST /users: Create a new user
- PUT /users/{id}: Update a single user
- DELETE /users/{id}: Delete a single user

Payments

- GET /payments: Retrieve a list of all payments
- GET /payments/{id}: Retrieve a single payment by ID
- POST /payments: Create a new payment
- PUT /payments/{id}: Update a single payment
- DELETE /payments/{id}: Delete a single payment

Transactions

- GET /transactions: Retrieve a list of all transactions
- GET /transactions/{id}: Retrieve a single transaction by ID
- POST /transactions: Create a new transaction
- PUT /transactions/{id}: Update a single transaction
- DELETE /transactions/{id}: Delete a single transaction

## Methods

### GET

- Retrieve a list of resources or a single resource by ID

### POST

- Create a new resource

### PUT

- Update a single resource

## DELETE

- Delete a single resource

## Request Headers

- Content-Type: application/json
- Authorization: Bearer <token>

## Response Codes

- 200 OK: Request successful
- 400 Bad Request: Invalid request
- 401 Unauthorized: Unauthorized access
- 404 Not Found: Resource not found
- 500 Internal Server Error: Server error

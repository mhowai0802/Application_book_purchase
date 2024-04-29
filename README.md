# Application_book_purchase
Frontend_backend_docker

`chmod +x start.sh`

`./start.sh`

Configuration to connect the mysql server in docker container

`mysql://root:123456@127.0.0.1:3307?statusColor=F8F8F8&env=local&name=Docker_testing_db&tLSMode=0&usePrivateKey=false&safeModeLevel=0&advancedSafeModeLevel=0&driverVersion=0&lazyload=true`

Query needed to be executed

`INSERT INTO User_info (name, password, phone_number)
VALUES 
  ('James Anderson', 'securePass789', '+852 5987 6543'),
  ('Sophia Thompson', 'myP@$$w0rd', '+852 2246 8135'),
  ('Benjamin Davis', 'strongPwd456', '+852 4789 1234'),
  ('Olivia Wilson', 'p@55w0rd!', '+852 9369 2584'),
  ('Liam Garcia', 'secrete987', '+852 1741 8529'),
  ('Lucas Robinson', 'strongP@55', '+852 9951 7532'),
  ('Ethan Lewis', 'mySecret123', '+852 9876 5431');`

  `INSERT INTO Book_info (title, categories, authors, ratings, price)
VALUES 
  ('The Great Gatsby', 'Fiction', 'F. Scott Fitzgerald', 4.5, 12.99),
  ('Pride and Prejudice', 'Romance', 'Jane Austen', 4.8, 9.99),
  ('The Catcher in the Rye', 'Fiction', 'J.D. Salinger', 4.2, 11.99),
  ('To Kill a Mockingbird', 'Fiction', 'Harper Lee', 4.7, 10.99),
  ('The Da Vinci Code', 'Mystery', 'Dan Brown', 4.3, 14.99),
  ('Harry Potter and the Sorcerer''s Stone', 'Fantasy', 'J.K. Rowling', 4.9, 13.99),
  ('1984', 'Fiction', 'George Orwell', 4.6, 12.99),
  ('The Hobbit', 'Fantasy', 'J.R.R. Tolkien', 4.7, 11.99),
  ('The Alchemist', 'Fiction', 'Paulo Coelho', 4.4, 9.99),
  ('The Hunger Games', 'Science Fiction', 'Suzanne Collins', 4.5, 10.99),
  ('The Lord of the Rings', 'Fantasy', 'J.R.R. Tolkien', 4.8, 19.99),
  ('The Girl on the Train', 'Mystery', 'Paula Hawkins', 4.2, 13.99),
  ('Romeo and Juliet', 'Romance', 'William Shakespeare', 4.6, 8.99),
  ('Gone Girl', 'Mystery', 'Gillian Flynn', 4.3, 12.99),
  ('The Chronicles of Narnia', 'Fantasy', 'C.S. Lewis', 4.7, 14.99),
  ('The Help', 'Fiction', 'Kathryn Stockett', 4.5, 11.99),
  ('The Fault in Our Stars', 'Young Adult', 'John Green', 4.4, 9.99),
  ('The Kite Runner', 'Fiction', 'Khaled Hosseini', 4.6, 12.99),
  ('The Maze Runner', 'Young Adult', 'James Dashner', 4.3, 10.99),
  ('The Girl with the Dragon Tattoo', 'Mystery', 'Stieg Larsson', 4.5, 11.99);`

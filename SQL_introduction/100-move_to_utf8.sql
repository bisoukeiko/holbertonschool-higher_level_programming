-- convert database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) 
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
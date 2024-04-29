FROM mysql:latest
# 設定環境變數
ENV MYSQL_DATABASE=Automate
ENV MYSQL_USER=automate
ENV MYSQL_PASSWORD=123456
ENV MYSQL_ROOT_PASSWORD=123456

# COPY my.cnf /etc/my.cnf
RUN echo '[mysqld]' >> /etc/my.cnf  \
    && echo "general_log = 1" >> /etc/my.cnf \
    && echo "general_log_file = /var/log/mysqld.log" >> /etc/my.cnf \
    && echo "log_output = file" >> /etc/my.cnf
    
# 指定路徑
WORKDIR /var/lib/mysql

# 指定容器運行時使用的預設命令
CMD ["mysqld"]
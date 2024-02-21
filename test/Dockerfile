# Этап 1: Компиляция и сборка приложения
FROM golang:1.21 AS build
WORKDIR /src
COPY . .
RUN go build -o /bin/hello ./main.go

# Этап 2: Формирование легковесного образа, запуск
FROM scratch AS run
COPY --from=build /bin/hello /bin/hello
CMD ["/bin/hello"]
# Use an image with Gradle
FROM gradle:7.5.1-jdk17 AS builder

# Copy project files to build image
COPY . /app
WORKDIR /app

# Build with Gradle
RUN gradle clean build --no-daemon

# Choose runtime image
FROM eclipse-temurin:21.0.2_13-jdk-jammy

# Add the executable jar file in this container
COPY build/libs/helloworld.jar /app/helloworld.jar
# Run the application when the container starts
ENTRYPOINT ["java", "-jar", "/app/helloworld.jar"]

EXPOSE 8080
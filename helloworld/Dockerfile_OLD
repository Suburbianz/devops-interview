FROM eclipse-temurin:21.0.2_13-jdk-jammy

# STEP 1: Add the executable jar file in this container
COPY build/libs/helloworld.jar /app/helloworld.jar
# STEP 2: Run the application when the container starts
ENTRYPOINT ["java", "-jar", "/app/helloworld.jar"]

EXPOSE 8080
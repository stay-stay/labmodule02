Setting a specific path for your configuration file, like `PiotConfig.props`, ensures that both the main application and any tests can easily find it, preventing errors related to missing files.
By organizing your code into a folder called `app` and creating a class named `ConstrainedDeviceApp`, you create a clear structure that makes it easier to manage. 
Logging acts like a diary for the application, recording important events such as when the app starts and stops, which helps track its behavior and diagnose issues. 
The `main()` function allows you to run the application smoothly, simulating real usage by starting it, waiting for 65 seconds, and then stopping it.
Writing tests to check whether your code works correctly, both in isolation and together, ensures that your application runs reliably and helps catch any problems early on.
Overall, these practices make your IoT application more organized, easier to understand, and more dependable.

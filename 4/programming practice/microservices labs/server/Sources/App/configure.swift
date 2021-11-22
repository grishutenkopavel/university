import Vapor
import Fluent
import FluentPostgresDriver
// configures your application
public func configure(_ app: Application) throws {
    // uncomment to serve files from /Public folder
    // app.middleware.use(FileMiddleware(publicDirectory: app.directory.publicDirectory))
  app.databases.use(.postgres(hostname: "localhost", username: "postgres", password: "", database: "hypotenusedb"), as: .psql)
  app.migrations.add(HypotenuseMigration())
    // register routes
    try routes(app)
}

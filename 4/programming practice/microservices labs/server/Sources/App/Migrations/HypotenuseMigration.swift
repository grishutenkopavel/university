//
//  File.swift
//  
//
//  Created by Павел Гришутенко on 22.11.2021.
//

import Foundation
import Fluent
import FluentPostgresDriver

struct HypotenuseMigration: Migration {
    func prepare(on database: Database) -> EventLoopFuture<Void> {
      database.schema("Hypotenuses")
        .id()
        .field("Hypotenuse", .string)
        .create()
    }

    func revert(on database: Database) -> EventLoopFuture<Void> {
      database.schema("Hypotenuses").delete()
    }
}

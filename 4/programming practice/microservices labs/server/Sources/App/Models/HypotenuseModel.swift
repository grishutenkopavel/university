//
//  File.swift
//  
//
//  Created by Павел Гришутенко on 22.11.2021.
//

import Foundation
import Vapor
import Fluent
import FluentPostgresDriver

final class HypotenuseModel: Content, Model {
  
  static let schema = "Hypotenuses"
  
  @ID(key: .id)
  var id: UUID?
  
  @Field(key: "Hypotenuse")
  var hypotenuse: String?
  
  init() { }
  
  init(id: UUID? = nil, hypotenuse: String) throws {
    self.id = id
    self.hypotenuse = hypotenuse
  }
}

//
//  File.swift
//  
//
//  Created by Павел Гришутенко on 27.10.2021.
//

import Foundation
import Vapor


struct APIController: RouteCollection {
    
    func boot(routes: RoutesBuilder) throws {
        let api = routes.grouped("api")
        api.get(use: index)
        
        api.group("json") { json in
            json.get(use: show)
            json.post(use: show)
        }
      api.post("hypotenuse") { req -> String in
        let hypotenuseAppRequest = HypotenuseAppRequest(request: req)
        return returnJsonMyStruct(result: hypotenuseAppRequest.result)
      }
    }

    func index(req: Request) throws -> String {
        return "hola"
    }
    
    func show(req: Request) throws -> String {
      return returnJsonMyStruct(result: "hello_world_app")
    }
  
  private func returnJsonMyStruct(result: String) -> String {
      let encoder = JSONEncoder()
      encoder.outputFormatting = .prettyPrinted
    
      var res = MyStructResponse()
      res.seccess = "seccess"
      res.result  = result
      res.version = "1.0"
    
      let data = try? encoder.encode(res)
      guard let data = data else { return "None"}
      return String(data: data, encoding: .utf8)!
    }
}

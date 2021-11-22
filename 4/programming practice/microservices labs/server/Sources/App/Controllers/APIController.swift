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
       // api.get(use: index)
        
        api.group("json") { json in
            json.get(use: show)
            json.post(use: show)
        }
      api.post("hypotenuse") { req -> String in
        let hypotenuseAppRequest = HypotenuseAppRequest(request: req)
        return returnJsonMyStruct(result: hypotenuseAppRequest.result)
      }
      //CRUD
      api.post("addHypotenuse") { req -> EventLoopFuture<HypotenuseModel> in
        let hypotenuse = try req.content.decode(HypotenuseModel.self)
        let hypotenuseAppRequest = HypotenuseAppRequest(request: req)
        hypotenuse.hypotenuse = hypotenuseAppRequest.result
        
        return hypotenuse.create(on: req.db).map { hypotenuse }
      }
      
      api.get("getHypotenuses") { req in
        HypotenuseModel.query(on: req.db).all()
      }
      
      api.post("updateHypotenuses") { req -> EventLoopFuture<HypotenuseModel> in
        let updatedHypotenuse = try req.content.decode(HypotenuseModel.self)
        return HypotenuseModel.find( updatedHypotenuse.id, on: req.db)
          .unwrap(or: Abort(.notFound)).flatMap { hypotenuse in
            hypotenuse.hypotenuse = updatedHypotenuse.hypotenuse
            return hypotenuse.save(on: req.db).map { hypotenuse }
        }
      }
      
      api.post("deleteHypotenuses") { req -> EventLoopFuture<HTTPStatus> in
        let hypotenuseInfoInput = try req.content.decode(HypotenuseModel.self)
        return HypotenuseModel.find(hypotenuseInfoInput.id, on: req.db)
          .flatMap { ($0?.delete(on: req.db))! }
          .map { .ok }
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

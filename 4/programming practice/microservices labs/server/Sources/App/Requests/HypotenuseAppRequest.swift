//
//  File.swift
//  
//
//  Created by Павел Гришутенко on 22.11.2021.
//

import Foundation
import Vapor

enum HypotenuseRequestError: Error {
  case CathetusTypeError
  case CathetusValueError
}

class HypotenuseAppRequest {
  private var cathetusA: Double?
  private var cathetusB: Double?
  private var hypotenuse: Double?
  var result: String = ""
  
  init(request: Request) {
    let cathetusData = try! request.content.decode(HypotenuseRequestData.self)
    self.cathetusA = Double(cathetusData.cathetusA)
    self.cathetusB = Double(cathetusData.cathetusB)
    do{
      hypotenuse = try calcHypotenuse()
      if let hypotenuse = self.hypotenuse {
        result = String(hypotenuse)
      }
    } catch HypotenuseRequestError.CathetusTypeError {
      result = "CathetusTypeError"
    } catch HypotenuseRequestError.CathetusValueError {
      result = "CathetusValueError"
    } catch {
      result = ""
    }
  }
  private func calcHypotenuse() throws -> Double {
    guard let cathetusA = cathetusA else { throw HypotenuseRequestError.CathetusTypeError }
    guard let cathetusB = cathetusB else { throw HypotenuseRequestError.CathetusTypeError }
    guard cathetusA > 0 else { throw HypotenuseRequestError.CathetusValueError }
    guard cathetusB > 0 else { throw HypotenuseRequestError.CathetusValueError }
    
    return sqrt(cathetusA * cathetusA + cathetusB * cathetusB)
  }
}

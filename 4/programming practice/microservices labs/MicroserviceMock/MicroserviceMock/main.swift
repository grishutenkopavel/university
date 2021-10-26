//
//  main.swift
//  MicroserviceMock
//
//  Created by Павел Гришутенко on 26.10.2021.
//

import Foundation


let url = URL(string: "https://www.yandex.ru")!

let task = URLSession.shared.dataTask(with: url) {(data, response, error) in
    guard let data = data else { return }
    print(String(data: data, encoding: .utf8)!)

}

task.resume()

while true {
    
}

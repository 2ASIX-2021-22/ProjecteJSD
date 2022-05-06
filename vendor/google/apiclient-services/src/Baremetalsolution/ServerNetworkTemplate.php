<?php
/*
 * Copyright 2014 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy of
 * the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under
 * the License.
 */

namespace Google\Service\Baremetalsolution;

class ServerNetworkTemplate extends \Google\Collection
{
  protected $collection_key = 'logicalInterfaces';
  /**
   * @var string[]
   */
  public $applicableInstanceTypes;
  protected $logicalInterfacesType = LogicalInterface::class;
  protected $logicalInterfacesDataType = 'array';
  /**
   * @var string
   */
  public $name;

  /**
   * @param string[]
   */
  public function setApplicableInstanceTypes($applicableInstanceTypes)
  {
    $this->applicableInstanceTypes = $applicableInstanceTypes;
  }
  /**
   * @return string[]
   */
  public function getApplicableInstanceTypes()
  {
    return $this->applicableInstanceTypes;
  }
  /**
   * @param LogicalInterface[]
   */
  public function setLogicalInterfaces($logicalInterfaces)
  {
    $this->logicalInterfaces = $logicalInterfaces;
  }
  /**
   * @return LogicalInterface[]
   */
  public function getLogicalInterfaces()
  {
    return $this->logicalInterfaces;
  }
  /**
   * @param string
   */
  public function setName($name)
  {
    $this->name = $name;
  }
  /**
   * @return string
   */
  public function getName()
  {
    return $this->name;
  }
}

// Adding a class alias for backwards compatibility with the previous class name.
class_alias(ServerNetworkTemplate::class, 'Google_Service_Baremetalsolution_ServerNetworkTemplate');
